import json
from time import time

from asyncpg import ForeignKeyViolationError, InFailedSQLTransactionError
from fastapi import Depends
from psycopg2 import errors
from sqlalchemy import exc
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from backend.entity_endpoints.models import CityModel, EventModel, ExcursionModel, RestaurantModel, HotelModel, RegionModel, \
    DataMlModel
from backend.database import get_async_session


async def add_city(city: CityModel, current_session: AsyncSession = Depends(get_async_session)):
    with open('17_dataset/cities.json', 'r', encoding='utf-8') as cities:
        data_cities = json.load(cities)
        for i in data_cities:
            try:
                stmt = insert(city).values(
                    id=i.get('_id').get('$oid'),
                    city_name=i.get('dictionary_data').get('title'),
                    rating=i.get('dictionary_data').get('rating'),
                    timezone=i.get('dictionary_data').get('timezone'),
                    geo_data=i.get('dictionary_data').get('geo_data').get('coordinates')
                ).on_conflict_do_nothing()
                await current_session.execute(stmt)
                await current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
    print('cities added')


async def add_event(event: EventModel, current_session: AsyncSession = Depends(get_async_session)):
    with open('17_dataset/events.json', 'r', encoding='utf-8') as events:
        data_events = json.load(events)
        for i in data_events:
            try:
                if len(i.get('dictionary_data').get('schedule')) != 0:
                    if isinstance(i.get('dictionary_data').get('schedule')[0].get('start'), dict):
                        stmt = insert(event).values(
                            id=i.get('_id').get('$oid'),
                            city_id=(i.get('dictionary_data').get('city') if i.get('dictionary_data').get(
                                'city') else 'null'),
                            start=i.get('dictionary_data').get('schedule')[0].get('start').get('$date'),
                            end=i.get('dictionary_data').get('schedule')[0].get('end').get('$date'),
                            price=(
                                float(
                                    i.get('dictionary_data').get('ticket_price') if i.get('dictionary_data').get(
                                        'ticket_price') else None
                                )
                            ),
                            bought_count=0
                        ).on_conflict_do_nothing()
                    else:
                        stmt = insert(event).values(
                            id=i.get('_id').get('$oid'),
                            city_id=i.get('dictionary_data').get('city'),
                            start=i.get('dictionary_data').get('schedule')[0].get('start'),
                            end=i.get('dictionary_data').get('schedule')[0].get('end'),
                            price=(
                                float(
                                    i.get('dictionary_data').get('ticket_price') if i.get('dictionary_data').get(
                                        'ticket_price') else None
                                )
                            ),
                            bought_count=0
                        ).on_conflict_do_nothing()
                    await current_session.execute(stmt)
                    await current_session.commit()
            except (
                    exc.IntegrityError,
                    exc.InternalError,
                    errors.ForeignKeyViolation,
                    errors.UniqueViolation,
                    ForeignKeyViolationError,
                    InFailedSQLTransactionError
            ) as e:
                continue
    print('events_added')


async def add_excursion(excursion: ExcursionModel, current_session: AsyncSession = Depends(get_async_session)):
    with open('17_dataset/excursions.json', 'r', encoding='utf-8') as excursions:
        data_excursions = json.load(excursions)
        for i in data_excursions:
            try:
                if isinstance(i.get('dictionary_data').get('season_start'), str):
                    stmt = insert(excursion).values(
                        id=i.get('_id').get('$oid'),
                        city_id=i.get('dictionary_data').get('city'),
                        start=i.get('dictionary_data').get('season_start'),
                        end=i.get('dictionary_data').get('season_end'),
                        price=i.get('dictionary_data').get('price'),
                        bought_count=0
                    ).on_conflict_do_nothing()
                else:
                    stmt = insert(excursion).values(
                        id=i.get('_id').get('$oid'),
                        city_id=i.get('dictionary_data').get('city'),
                        start=i.get('dictionary_data').get('season_start').get('$date'),
                        end=i.get('dictionary_data').get('season_end').get('$date'),
                        price=i.get('dictionary_data').get('price'),
                        bought_count=0
                    ).on_conflict_do_nothing()
                await current_session.execute(stmt)
                await current_session.commit()
            except (
                    exc.IntegrityError,
                    exc.InternalError,
                    errors.ForeignKeyViolation,
                    errors.UniqueViolation,
                    ForeignKeyViolationError
            ) as e:
                print(e)
    print('excursions_added')


async def add_hotel(hotel: HotelModel, current_session: AsyncSession = Depends(get_async_session)):
    with open('17_dataset/hotels.json', 'r', encoding='utf-8') as hotels:
        data_hotels = json.load(hotels)
        for i in data_hotels:
            try:
                stmt = insert(hotel).values(
                    id=i.get('_id').get('$oid'),
                    address=i.get('dictionary_data').get('address'),
                    geo_data=i.get('dictionary_data').get('geo_data').get('coordinates'),
                    city_id=i.get('dictionary_data').get('city'),
                    title=i.get('dictionary_data').get('title'),
                    bought_count=0
                ).on_conflict_do_nothing()
                await current_session.execute(stmt)
                await current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
    print('hotels_added')


async def add_region(region: RegionModel, current_session: AsyncSession = Depends(get_async_session)):
    with open('17_dataset/regions.json', 'r', encoding='utf-8') as regions:
        data_regions = json.load(regions)
        for i in data_regions:
            try:
                stmt = insert(region).values(
                    id=i.get('_id').get('$oid'),
                    title=i.get('dictionary_data').get('title'),
                    price_hotel=i.get('dictionary_data').get('price_hotel')
                ).on_conflict_do_nothing()
                await current_session.execute(stmt)
                await current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
    print('regions_added')


async def add_restaurant(restaurant: RestaurantModel, current_session: AsyncSession = Depends(get_async_session)):
    with open('17_dataset/restaurants.json', 'r', encoding='utf-8') as restaurants:
        data_restaurants = json.load(restaurants)
        for i in data_restaurants:
            try:
                if i.get('dictionary_data').get('geo_data') is not None:
                    stmt = insert(restaurant).values(
                        id=i.get('_id').get('$oid'),
                        city_id=i.get('dictionary_data').get('city')[0],
                        geo_data=i.get(
                            'dictionary_data'
                        ).get('geo_data').get('coordinates'),
                        name=i.get('dictionary_data').get('title'),
                        kitchen_type=i.get('dictionary_data').get('cuisines'),
                        mean_price=i.get('dictionary_data').get('bill'),
                        bought_count=0
                    ).on_conflict_do_nothing()
                await current_session.execute(stmt)
                await current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
    print('restaurants_added')


async def add_item(item: DataMlModel, current_session: AsyncSession = Depends(get_async_session)):
    files = ['17_dataset/excursions.json', '17_dataset/events.json',
             '17_dataset/hotels.json', '17_dataset/restaurants.json']
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for i in data:
                try:
                    stmt = insert(item).values(
                        item_id=i.get('_id').get('$oid'),
                        user_id=None,
                        bought=0
                    ).on_conflict_do_nothing()
                    await current_session.execute(stmt)
                except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                    continue
            await current_session.commit()
    print('items_added')


async def fill():
    func_list = [
        (add_city, CityModel),
        (add_event, EventModel),
        (add_excursion, ExcursionModel),
        (add_restaurant, RestaurantModel),
        (add_hotel, HotelModel),
        (add_region, RegionModel),
    ]

    for func in func_list:
        async for session in get_async_session():

            try:
                await func[0](func[1], session)
            except (
                    exc.IntegrityError,
                    exc.InternalError,
                    errors.ForeignKeyViolation,
                    errors.UniqueViolation,
                    ForeignKeyViolationError,
                    exc.DBAPIError
            ) as e:
                print(e)


def main():
    import asyncio
    start = time()
    asyncio.run(fill())
    print(time() - start)


main()
