from fastapi import APIRouter
from backend.identity_endpoints.auth.router import router as auth_router
from backend.identity_endpoints.registration.router import router as registration_router

aggregated_router = APIRouter()

routers = (
    auth_router,
    registration_router,
)

for router in routers:
    aggregated_router.include_router(
        router,
    )

