from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.analysis.routers import event
from src.analysis.routers import recommendation
from src.analysis.routers import region, hotel, excursion, city, restaurant
from src.identity_endpoints.routers import aggregated_router as identity_routers


app = FastAPI(
    title='RUSSPASS recommendation service',
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


app.include_router(
    identity_routers,
    prefix='/identity',
    tags=['Identification'],
)


app.include_router(city.router)
app.include_router(event.router)
app.include_router(excursion.router)
app.include_router(hotel.router)
app.include_router(region.router)
app.include_router(restaurant.router)
app.include_router(recommendation.router)
