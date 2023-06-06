from typing import Annotated

import pandas as pd
from fastapi import Depends
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

from backend.identity_endpoints.logic import get_current_active_user
from backend.identity_endpoints.schemas import UserInDB


async def recommend_event(
        list_dict: list,
        username: str,
        item_id,
        recommendations=10
):
    items = pd.DataFrame(list_dict)
    user_matrix = pd.pivot_table(
        items,
        index=['item_id'],
        columns=['username'],
        values=['bought']
    ).fillna(0)
    user_data = csr_matrix(user_matrix.values)
    user_item_matrix = user_matrix.rename_axis(None, axis=0).reset_index()
    ml_model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
    ml_model.fit(user_data)
    print(user_matrix)
    print()
    print(user_item_matrix)
    username = user_item_matrix[user_item_matrix['index'] == item_id].index[0]
    indices = ml_model.kneighbors(
        user_data[username],
        n_neighbors=3
    )[1][0]

    # indices_distances = list(zip(indices, distances))
    # print(indices_distances)
    # result = sorted(indices_distances, key=lambda x: x[1], reverse=False)[1:]
    return indices
