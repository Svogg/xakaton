import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from xakaton.src.database import get_async_session
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from sqlalchemy import select


async def recommend_event(username, session: AsyncSession = Depends(get_async_session), recommendations=10):
    items = pd.read_sql_query('SELECT * from mldata;', con=session)
    print(items)
    user_matrix = items.pivot(index='item_id',
                              columns='username',
                              values='bought').fillna(0, inplace=True)
    user_data = csr_matrix(user_matrix.values)
    user_item_matrix = user_matrix.rename_axis(None, axis=1).reset_index()
    ml_model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
    ml_model.fit(user_data)
    username = user_item_matrix[user_item_matrix['username'] == username].index[0]
    distances, indices = ml_model.kneighbors(user_data[username],
                                             n_neighbors=recommendations + 1).squeeze().tolist()
    indices_distances = list(zip(indices, distances))
    result = sorted(indices_distances, key=lambda x: x[1], reverse=False)[1:]
    return [i[0] for i in result]
