from fastapi import APIRouter
from src.identity_endpoints.auth.router import router as auth_router
from src.identity_endpoints.registration.router import router as registration_router

aggregated_router = APIRouter()

aggregated_router.include_router(
    auth_router,
)
aggregated_router.include_router(
    registration_router,
)
