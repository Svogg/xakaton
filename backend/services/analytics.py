import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


async def recommend_event(
        list_dict: list,
        username: str
):
    items = pd.DataFrame(list_dict)
    user_matrix = pd.pivot_table(
        items,
        index=['username'],
        columns=['item_id'],
        values=['bought']
    ).fillna(0)
    user_data = csr_matrix(user_matrix.values)
    user_item_matrix = user_matrix.rename_axis(None, axis=0).reset_index()
    ml_model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
    ml_model.fit(user_data)
    user = user_item_matrix[user_item_matrix['index'] == username].index[0]
    indices = ml_model.kneighbors(
        user_data[user],
        n_neighbors=3
    )[1][0]
    return indices


def most_favour(data):
    result = {}
    for elem in data:
        if elem['item_id'] not in result:
            result.update({elem['item_id']: 0})
        result[elem['item_id']] += 1
    return {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
