from fastapi import APIRouter
from backend.entity_endpoints.city.router import router as city_router
from backend.entity_endpoints.event.router import router as event_router
from backend.entity_endpoints.excursion.router import router as excursion_router
from backend.entity_endpoints.hotel.router import router as hotel_router
from backend.entity_endpoints.region.router import router as region_router
from backend.entity_endpoints.restaurant.router import router as restaurant_router
from backend.entity_endpoints.recommendation.router import router as recommendation_router

aggregated_router = APIRouter()

routers = (
    city_router,
    event_router,
    excursion_router,
    hotel_router,
    region_router,
    restaurant_router,
    recommendation_router,
)

for router in routers:
    aggregated_router.include_router(
        router,
    )

