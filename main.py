from fastapi import FastAPI
from src.analysis.routers import event
from src.analysis.routers import region, hotel, excursion, city, restaurant

app = FastAPI(
    titel='Russpass recommendation service'
)


app.include_router(city.router)
app.include_router(event.router)
app.include_router(excursion.router)
app.include_router(hotel.router)
app.include_router(region.router)
app.include_router(restaurant.router)


