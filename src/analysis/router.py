import asyncio
import json
from time import time
from fastapi import APIRouter, Depends

from psycopg2 import errors
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from .models import CityModel, EventModel, ExcursionModel, RestaurantModel, HotelModel, RegionModel, RouteModel, TrackModel
from .schemas import CitySchema, EventSchema, ExcursionSchema, RestaurantSchema


router = APIRouter()

async def add_city(city: CitySchema, current_session: AsyncSession = Depends(get_async_session)):
    with open('17_dataset/cities.json', 'r', encoding='utf-8') as cities:
        data_cities = json.load(cities)
        for i in data_cities:
            try:
                stmt = insert(city).values(CityModel(
                    id=i.get('_id').get('$oid'),
                    city_name=i.get('dictionary_data').get('title'),
                    rating=i.get('dictionary_data').get('rating'),
                    timezone=i.get('dictionary_data').get('timezone'),
                    geo_data=i.get('dictionary_data').get('geo_data').get('coordinates')
                )).on_conflict_do_nothing()
                await current_session.execute(stmt)
                await current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue



# @router.post('/add_track')
# async def add_track(track: Track, current_session: get_async_session):
#     async with open('17_dataset/tracks.json', 'r', encoding='utf-8') as tracks:
#         data_tracks = await json.load(tracks)
#         for i in data_tracks:
#             try:
#                 stmt = insert(track).values(
#                     id=i.get('_id').get('$oid'),
#                     city_id=i.get('dictionary_data').get('city'),
#                     region=i.get('dictionary_data').get('region'),
#                     days_count=i.get('dictionary_data').get('days_count'),
#                     description=i.get('dictionary_data').get('description'),
#                     price=i.get('dictionary_data').get('price')
#                 ).on_conflict_do_nothing()
#                 await current_session.execute(stmt)
#                 await current_session.commit()
#             except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
#                 continue
#         print('tracks_added')


@router.post('/add_event')
async def add_event(event: EventSchema, current_session: AsyncSession = Depends(get_async_session)):
    with open('17_dataset/events.json', 'r', encoding='utf-8') as events:
        data_events = await json.load(events)
        for i in data_events:
            try:
                if len(i.get('dictionary_data').get('schedule')) != 0:
                    if isinstance(i.get('dictionary_data').get('schedule')[0].get('start'), dict):
                        stmt = insert(event).values(EventModel(
                            id=i.get('_id').get('$oid'),
                            city_id=(i.get('dictionary_data').get('city') if i.get('dictionary_data').get(
                                'city') else 'null'),
                            start=i.get('dictionary_data').get('schedule')[0].get('start').get('$date'),
                            end=i.get('dictionary_data').get('schedule')[0].get('end').get('$date'),
                            price=i.get('dictionary_data').get('ticket_price')
                        )).on_conflict_do_nothing()
                    else:
                        stmt = insert(event).values(
                            id=i.get('_id').get('$oid'),
                            city_id=i.get('dictionary_data').get('city'),
                            start=i.get('dictionary_data').get('schedule')[0].get('start'),
                            end=i.get('dictionary_data').get('schedule')[0].get('end'),
                            price=i.get('dictionary_data').get('ticket_price')
                        ).on_conflict_do_nothing()
                    await current_session.execute(stmt)
                    await current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
        print('events_added')


@router.post('/add_excursion')
async def add_excursion(excursion: ExcursionSchema, current_session: AsyncSession = Depends(get_async_session)):
    with open('17_dataset/excursions.json', 'r', encoding='utf-8') as excursions:
        data_excursions = await json.load(excursions)
        for i in data_excursions:
            try:
                if isinstance(i.get('dictionary_data').get('season_start'), str):
                    stmt = insert(excursion).values(ExcursionModel(
                        id=i.get('_id').get('$oid'),
                        city_id=i.get('dictionary_data').get('city'),
                        start=i.get('dictionary_data').get('season_start'),
                        end=i.get('dictionary_data').get('season_end'),
                        price=i.get('dictionary_data').get('price')
                    )).on_conflict_do_nothing()
                else:
                    stmt = insert(excursion).values(ExcursionModel(
                        id=i.get('_id').get('$oid'),
                        city_id=i.get('dictionary_data').get('city'),
                        start=i.get('dictionary_data').get('season_start').get('$date'),
                        end=i.get('dictionary_data').get('season_end').get('$date'),
                        price=i.get('dictionary_data').get('price')
                    )).on_conflict_do_nothing()
                await current_session.execute(stmt)
                await current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                print(e)
        print('excursions_added')


# @router.post('/add_hotel')
# async def add_hotel(hotel: Hotel, current_session: get_async_session):
#     async with open('17_dataset/hotels.json', 'r', encoding='utf-8') as hotels:
#         data_hotels = await json.load(hotels)
#         for i in data_hotels:
#             try:
#                 stmt = insert(hotel).values(
#                     id=i.get('_id').get('$oid'),
#                     address=i.get('dictionary_data').get('address'),
#                     geo_data=i.get('dictionary_data').get('geo_data').get('coordinates'),
#                     city_id=i.get('dictionary_data').get('city'),
#                     title=i.get('dictionary_data').get('title')
#                 ).on_conflict_do_nothing()
#                 await current_session.execute(stmt)
#                 await current_session.commit()
#             except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
#                 continue
#         print('hotels_added')


# @router.post('/add_region')
# async def add_region(region: Region, current_session: get_async_session):
#     async with open('17_dataset/regions.json', 'r', encoding='utf-8') as regions:
#         data_regions = await json.load(regions)
#         for i in data_regions:
#             try:
#                 stmt = insert(region).values(
#                     id=i.get('_id').get('$oid'),
#                     title=i.get('dictionary_data').get('title'),
#                     price_hotel=i.get('dictionary_data').get('price_hotel')
#                 ).on_conflict_do_nothing()
#                 await current_session.execute(stmt)
#                 await current_session.commit()
#             except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
#                 continue
#         print('regions_added')


# @router.post('/add_route')
# async def add_route(route: Route, current_session: get_async_session):
#     async with open('17_dataset/routes.json', 'r', encoding='utf-8') as routes:
#         data_routes = await json.load(routes)
#         for i in data_routes:
#             try:
#                 stmt = insert(route).values(
#                     id=i.get('_id').get('$oid'),
#                     title=i.get('dictionary_data').get('title'),
#                     time=i.get('dictionary_data').get('time'),
#                     city_id=i.get('dictionary_data').get('city')
#                 ).on_conflict_do_nothing()
#                 await current_session.execute(stmt)
#                 await current_session.commit()
#             except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
#                 continue
#         print('routes_added')


@router.post('/add_restaurant')
async def add_restaurant(restaurant: RestaurantSchema, current_session: AsyncSession = Depends(get_async_session)):
    with open('17_dataset/restaurants.json', 'r', encoding='utf-8') as restaurants:
        data_restaurants = await json.load(restaurants)
        for i in data_restaurants:
            try:
                if i.get('dictionary_data').get('geo_data') is not None:
                    stmt = insert(restaurant).values(RestaurantModel(
                        id=i.get('_id').get('$oid'),
                        city_id=i.get('dictionary_data').get('city')[0],
                        geo_data=i.get(
                            'dictionary_data'
                        ).get('geo_data').get('coordinates'),
                        name=i.get('dictionary_data').get('title'),
                        kitchen_type=i.get('dictionary_data').get('cuisines'),
                        mean_price=i.get('dictionary_data').get('bill')
                    )).on_conflict_do_nothing()
                await current_session.execute(stmt)
                await current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
        print('restaurants_added')
