from fastapi import FastAPI
from src.analysis.routers import region, hotel, excursion, city, restaurant, event, recommendation
from src.identity_services.registration.router import router as router_registration
from src.identity_services.auth.router import router as auth_router

app = FastAPI(
    titel='Russpass recommendation service'
)


app.include_router(city.router)
app.include_router(event.router)
app.include_router(excursion.router)
app.include_router(hotel.router)
app.include_router(region.router)
app.include_router(restaurant.router)
app.include_router(recommendation.router)

app.include_router(
    router_registration,
    prefix='/registration',
    tags=['/registration']
)


app.include_router(
    auth_router,
    prefix='/auth',
    tags=['/auth']
)

