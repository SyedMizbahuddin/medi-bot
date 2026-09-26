"""JWT authentication middleware for protected API requests."""

from collections.abc import Awaitable, Callable

from fastapi import Request
from fastapi.responses import JSONResponse, Response
from starlette.middleware.base import BaseHTTPMiddleware

import jwt

from src.services.api.auth_service import AuthService
from starlette.types import ASGIApp

class JWTMiddleware(BaseHTTPMiddleware):
    """Validate bearer JWTs before forwarding protected requests."""

    _PUBLIC_PATHS = {"/health", "/login", "/docs", "/redoc", "/openapi.json"}

    def __init__(self, app: ASGIApp, auth_service: AuthService) -> None:
        """Initialize middleware with the injected authentication service."""
        super().__init__(app)
        self.auth_service = auth_service

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        """Authenticate protected requests and attach claims to request state."""
        if request.method == "OPTIONS" or self._is_public_path(request.url.path):
            return await call_next(request)

        authorization = request.headers.get("Authorization", "")
        scheme, _, token = authorization.partition(" ")
        if scheme.lower() != "bearer" or not token:
            return self._unauthorized("Missing bearer token")

        try:
            claims = self.auth_service.decode_access_token(token)
        except jwt.InvalidTokenError:
            return self._unauthorized("Invalid or expired token")

        request.state.jwt_claims = claims
        return await call_next(request)

    
    @classmethod
    def _is_public_path(cls, path: str) -> bool:
        """Return whether a path does not require JWT authentication."""
        return path in cls._PUBLIC_PATHS or path.startswith("/docs/") or path.startswith("/redoc/")

    
    @staticmethod
    def _unauthorized(detail: str) -> JSONResponse:
        """Create a standard unauthorized response."""
        return JSONResponse(status_code=401, content={"detail": detail})
