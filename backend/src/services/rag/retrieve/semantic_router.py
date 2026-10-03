"""Semantic routing for MediAssist queries."""

import logging

from semantic_router import Route, SemanticRouter
from semantic_router.encoders import FastEmbedEncoder

from src.config.app_config import app_settings
from src.helpers.router_questions import (
    HYBRID_RAG_QUESTIONS,
    SQL_RAG_QUESTIONS,
    UNRELATED_QUESTIONS,
)
from src.utils.constants import Role, RouteCategory

logger = logging.getLogger(__name__)


class MySemanticRouter:
    """Classify queries into vector, SQL, or unrelated routes."""

    _SQL_ROLES = {Role.ADMIN, Role.BILLING_EXECUTIVE}

    def __init__(self) -> None:
        """Create the semantic router and initialize its local index."""
        self.router = self.initialize()

    def initialize(self) -> SemanticRouter:
        """Build and return the semantic router from configured examples."""
        routes = [
            Route(
                name=RouteCategory.VECTOR_DB.value,
                utterances=HYBRID_RAG_QUESTIONS,
            ),
            Route(
                name=RouteCategory.SQL.value,
                utterances=SQL_RAG_QUESTIONS,
            ),
            Route(
                name=RouteCategory.UNRELATED.value,
                utterances=UNRELATED_QUESTIONS,
            ),
        ]

        logger.info("Initializing semantic router with %d routes", len(routes))
        router = SemanticRouter(
            encoder=FastEmbedEncoder(cache_dir=str(app_settings.ROUTER_DIR)),
            routes=routes,
            auto_sync="local",
        )
        logger.info("Semantic router initialized")
        return router

    def get_route(self, query: str, role: Role) -> RouteCategory:
        """Classify a query and enforce SQL-route role permissions.

        SQL retrieval is available only to administrators and billing
        executives. Unauthorized SQL-like queries are sent to vector retrieval
        so the SQL database is never queried for those roles. Empty queries and
        unrecognized router results use vector retrieval as the safe default.
        """
        if not query.strip():
            logger.info("Empty query; using vector route")
            return RouteCategory.VECTOR_DB

        choice = self.router(query)
        route_name = getattr(choice, "name", None)
        if not isinstance(route_name, str):
            logger.warning("Semantic router returned no route for query")
            return RouteCategory.VECTOR_DB

        try:
            category = RouteCategory(route_name)
        except ValueError:
            logger.warning("Unknown semantic route %s; using vector route", route_name)
            return RouteCategory.VECTOR_DB

        if category is RouteCategory.SQL and role not in self._SQL_ROLES:
            logger.warning("Role %s is not allowed to use SQL retrieval", role.value)
            return RouteCategory.VECTOR_DB

        logger.info("Selected %s route for role %s", category.value, role.value)
        return category
