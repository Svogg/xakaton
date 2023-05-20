import json

from sqlalchemy import insert

from config import DATABASE_URL

from create_schemas import get_session
from schemas import City

# with open('17_dataset/cities.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     for i in data:
#         if i['dictionary_data'].get('city'):
#             print(i['dictionary_data'].get('city'))


def add_city(new_city: City, session: get_session()):
    with open('17_dataset/cities.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in data:
            if i['dictionary_data'].get('city'):
                stmt = (
                    insert(City).
                    values(
                        new_city['id'] = i['dictionary_data']['city'],

                    )
                )
                session.execute(stmt)
                session.commit()

