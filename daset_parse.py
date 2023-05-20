import json
from time import time

from psycopg2 import errors
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import exc

from create_schemas import get_session, Session
from models import City, Event, Excursion, Restaurant


def add_city(city: City, current_session: Session):
    with open('17_dataset/cities.json', 'r', encoding='utf-8') as cities:
        data_cities = json.load(cities)

        for i in data_cities:
            stmt = insert(city).values(
                id=i.get('_id').get('$oid'),
                city_name=i.get('dictionary_data').get('title'),
                rating=i.get('dictionary_data').get('rating'),
                timezone=i.get('dictionary_data').get('timezone'),
                geo_data=i.get('dictionary_data').get('geo_data').get('coordinates')
            ).on_conflict_do_nothing()
            current_session.execute(stmt)
            print('city_added')
            current_session.commit()


def add_event(event: Event, current_session: Session):
    with open('17_dataset/events.json', 'r', encoding='utf-8') as events:
        data_events = json.load(events)
        for i in data_events:
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
                    print('event_added')
                    current_session.commit()


def add_excursion(excursion: Excursion, current_session: Session):
    with open('17_dataset/excursions.json', 'r', encoding='utf-8') as excursions:
        data_excursions = json.load(excursions)
        for i in data_excursions:
            if i.get('dictionary_data').get('route'):
                if len(i.get('dictionary_data').get('route')[0].get('events')):
                    if len(i.get('dictionary_data').get('route')[0].get('events')[0].get('geo_data').get('coordinates')):
                        if isinstance(i.get('dictionary_data').get('season_start'), str):
                            stmt = insert(excursion).values(
                                id=i.get('_id').get('$oid'),
                                city_id=i.get('dictionary_data').get('city'),
                                geo_data=i.get('dictionary_data').get('route')[0].get('events')[0].get('geo_data').get(
                                    'coordinates'),
                                start=i.get('dictionary_data').get('season_start'),
                                end=i.get('dictionary_data').get('season_end'),
                                price=i.get('dictionary_data').get('price')
                            ).on_conflict_do_nothing()
                            current_session.execute(stmt)
                            print('excursion_added')
                            current_session.commit()
                        else:
                            stmt = insert(excursion).values(
                                id=i.get('_id').get('$oid'),
                                city_id=i.get('dictionary_data').get('city'),
                                geo_data=i.get('dictionary_data').get('route')[0].get('events')[0].get('geo_data').get(
                                    'coordinates'),
                                start=i.get('dictionary_data').get('season_start').get('$date'),
                                end=i.get('dictionary_data').get('season_end').get('$date'),
                                price=i.get('dictionary_data').get('price')
                            ).on_conflict_do_nothing()
                            current_session.execute(stmt)
                            print('excursion_added')
                            current_session.commit()
                    else:
                        if isinstance(i.get('dictionary_data').get('season_start'), str):
                            stmt = insert(excursion).values(
                                id=i.get('_id').get('$oid'),
                                city_id=i.get('dictionary_data').get('city'),
                                start=i.get('dictionary_data').get('season_start'),
                                end=i.get('dictionary_data').get('season_end'),
                                price=i.get('dictionary_data').get('price')
                            ).on_conflict_do_nothing()
                            current_session.execute(stmt)
                            print('excursion_added')
                            current_session.commit()
                        else:
                            stmt = insert(excursion).values(
                                id=i.get('_id').get('$oid'),
                                city_id=i.get('dictionary_data').get('city'),
                                start=i.get('dictionary_data').get('season_start').get('$date'),
                                end=i.get('dictionary_data').get('season_end').get('$date'),
                                price=i.get('dictionary_data').get('price')).on_conflict_do_nothing()
                        current_session.execute(stmt)
                        print('excursion_added')
                        current_session.commit()


def add_hotel(current_session: Session):
    with open('17_dataset/hotels.json', 'r', encoding='utf-8') as hotels:
        data_hotels = json.load(hotels)
        ...


def add_restaurant(restaurant: Restaurant, current_session: Session):
    with open('17_dataset/restaurants.json', 'r', encoding='utf-8') as restaurants:

        data_restaurants = json.load(restaurants)

        for i in data_restaurants:
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
                print('restaurant_added')
                current_session.commit()


start = time()
for session in get_session():
    try:
        add_city(City, session)
    except (exc.IntegrityError, errors.ForeignKeyViolation, errors.UniqueViolation):

        print('city_error')
        continue

    session.commit()

for session in get_session():
    try:
        add_event(Event, session)
    except (exc.IntegrityError, errors.ForeignKeyViolation, errors.UniqueViolation):

        print('event_error')
        continue
    session.commit()

for session in get_session():
    try:
        add_excursion(Excursion, session)
    except (exc.IntegrityError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:

        print('excursion_error: {}'.format(e))
        continue
    session.commit()

for session in get_session():
    try:
        add_restaurant(Restaurant, session)
    except (exc.IntegrityError, errors.ForeignKeyViolation, errors.UniqueViolation) as e:

        print('restourant_error: {}'.format(e))
        continue
    session.commit()

print(time() - start)
