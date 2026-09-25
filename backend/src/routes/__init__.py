"""HTTP route composition for the MediAssist API."""

from fastapi import APIRouter

from src.routes import auth, chat

router = APIRouter()
router.include_router(auth.router)
router.include_router(chat.router)
