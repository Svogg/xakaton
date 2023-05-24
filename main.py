from fastapi import FastAPI
from src.routers import city, event, excursion, hotel, region, restaurant, route, track

app = FastAPI(
    titel='Russpass recommendation service'
)


app.include_router(city.router)
app.include_router(event.router)
app.include_router(excursion.router)
app.include_router(hotel.router)
app.include_router(region.router)
app.include_router(restaurant.router)
app.include_router(route.router)
app.include_router(track.router)

