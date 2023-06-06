import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from xakaton.src.database import engine
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from sqlalchemy import select


async def recommend_event(username, data, recommendations=10):
    # items = pd.read_sql_table(data, con=engine)
    items = pd.DataFrame(
        {'item_id': [i[0] for i in data],
         'username': [i[1] for i in data],
         'bought': [i[2] for i in data]
         })
    user_matrix = pd.pivot_table(items, index=['username'],
                                 columns=['item_id'],
                                 values=['bought']).fillna(0)
    user_data = csr_matrix(user_matrix.values)
    user_item_matrix = user_matrix.rename_axis(None, axis=0).reset_index()
    print(user_item_matrix)
    ml_model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=1, n_jobs=-1)
    ml_model.fit(user_data)
    username = user_item_matrix[user_item_matrix['index'] == username].index[0]
    # print(username)
    distances, indices = ml_model.kneighbors(user_data[username],
                                             n_neighbors=recommendations + 1).squeeze().tolist()
    indices_distances = list(zip(indices, distances))
    result = sorted(indices_distances, key=lambda x: x[1], reverse=False)[1:]
    return [i[0] for i in result]
