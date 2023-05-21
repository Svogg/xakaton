import json
from time import time

from psycopg2 import errors
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import exc

from xakaton.src.create_schemas import get_session, Session
from models import City, Event, Excursion, Restaurant, Hotel, Region, Route, Track


def add_city(city: City, current_session: Session):
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
                current_session.execute(stmt)
                current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
        print('cities_added')


def add_track(track: Track, current_session: Session):
    with open('17_dataset/tracks.json', 'r', encoding='utf-8') as tracks:
        data_tracks = json.load(tracks)
        for i in data_tracks:
            try:
                stmt = insert(track).values(
                    id=i.get('_id').get('$oid'),
                    city_id=i.get('dictionary_data').get('city'),
                    region=i.get('dictionary_data').get('region'),
                    days_count=i.get('dictionary_data').get('days_count'),
                    description=i.get('dictionary_data').get('description'),
                    price=i.get('dictionary_data').get('price')
                ).on_conflict_do_nothing()
                current_session.execute(stmt)
                current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
        print('tracks_added')



def add_event(event: Event, current_session: Session):
    with open('17_dataset/events.json', 'r', encoding='utf-8') as events:
        data_events = json.load(events)
        for i in data_events:
            try:
                if len(i.get('dictionary_data').get('schedule')) != 0:
                    if isinstance(i.get('dictionary_data').get('schedule')[0].get('start'), dict):
                        stmt = insert(Event).values(
                            id=i.get('_id').get('$oid'),
                            city_id=(i.get('dictionary_data').get('city') if i.get('dictionary_data').get(
                                'city') else 'null'),
                            start=i.get('dictionary_data').get('schedule')[0].get('start').get('$date'),
                            end=i.get('dictionary_data').get('schedule')[0].get('end').get('$date'),
                            price=i.get('dictionary_data').get('ticket_price')
                        ).on_conflict_do_nothing()
                        current_session.execute(stmt)
                        current_session.commit()
                    else:
                        stmt = insert(event).values(
                            id=i.get('_id').get('$oid'),
                            city_id=i.get('dictionary_data').get('city'),
                            start=i.get('dictionary_data').get('schedule')[0].get('start'),
                            end=i.get('dictionary_data').get('schedule')[0].get('end'),
                            price=i.get('dictionary_data').get('ticket_price')
                        ).on_conflict_do_nothing()
                        current_session.execute(stmt)
                        current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
        print('events_added')


def add_excursion(excursion: Excursion, current_session: Session):
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
                        price=i.get('dictionary_data').get('price')
                    ).on_conflict_do_nothing()
                else:
                    stmt = insert(excursion).values(
                        id=i.get('_id').get('$oid'),
                        city_id=i.get('dictionary_data').get('city'),
                        start=i.get('dictionary_data').get('season_start').get('$date'),
                        end=i.get('dictionary_data').get('season_end').get('$date'),
                        price=i.get('dictionary_data').get('price')).on_conflict_do_nothing()
                current_session.execute(stmt)
                current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                print(e)
        print('excursions_added')


def add_hotel(hotel: Hotel, current_session: Session):
    with open('17_dataset/hotels.json', 'r', encoding='utf-8') as hotels:
        data_hotels = json.load(hotels)
        for i in data_hotels:
            try:
                stmt = insert(hotel).values(
                    id=i.get('_id').get('$oid'),
                    address=i.get('dictionary_data').get('address'),
                    geo_data=i.get('dictionary_data').get('geo_data').get('coordinates'),
                    city_id=i.get('dictionary_data').get('city'),
                    title=i.get('dictionary_data').get('title')
                ).on_conflict_do_nothing()
                current_session.execute(stmt)
                current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
        print('hotels_added')


def add_region(region: Region, current_session: Session):
    with open('17_dataset/regions.json', 'r', encoding='utf-8') as regions:
        data_regions = json.load(regions)
        for i in data_regions:
            try:
                stmt = insert(region).values(
                    id=i.get('_id').get('$oid'),
                    title=i.get('dictionary_data').get('title'),
                    price_hotel=i.get('dictionary_data').get('price_hotel')
                ).on_conflict_do_nothing()
                current_session.execute(stmt)
                current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
        print('regions_added')


def add_route(route: Route, current_session: Session):
    with open('17_dataset/routes.json', 'r', encoding='utf-8') as routes:
        data_routes = json.load(routes)
        for i in data_routes:
            try:
                stmt = insert(route).values(
                    id=i.get('_id').get('$oid'),
                    title=i.get('dictionary_data').get('title'),
                    time=i.get('dictionary_data').get('time'),
                    city_id=i.get('dictionary_data').get('city')
                ).on_conflict_do_nothing()
                current_session.execute(stmt)
                current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
        print('routes_added')


def add_restaurant(restaurant: Restaurant, current_session: Session):
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
                        mean_price=i.get('dictionary_data').get('bill')
                    ).on_conflict_do_nothing()
                    current_session.execute(stmt)
                    current_session.commit()
            except (exc.IntegrityError, exc.InternalError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:
                continue
        print('restaurants_added')


func_list = [
        (add_city, City),
        (add_event, Event),
        (add_excursion, Excursion),
        (add_restaurant, Restaurant),
        (add_hotel, Hotel),
        (add_region, Region),
        (add_route, Route),
        (add_track, Track),
]


start = time()

for func in func_list:
    for session in get_session():
        func[0](func[1], session)

print(time() - start)
