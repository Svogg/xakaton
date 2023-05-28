from fastapi import FastAPI
from src.analysis.routers import region, hotel, excursion, city, restaurant, event, recommendation
from src.identity_services.registration.router import router as router_registration
from src.identity_services.auth.router import router as auth_router
from fastapi import FastAPI
from src.analysis.routers import event
from src.analysis.routers import region, hotel, excursion, city, restaurant
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    titel='Russpass recommendation service'
)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(city.router)

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

