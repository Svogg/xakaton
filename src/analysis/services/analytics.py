import pandas as pd
from src.database import engine
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


def recommend_event(user_id, recommendations=5):
    items = pd.read_sql_table('mldata', columns=['item_id', 'user_id', 'bought'], con=engine)
    user_matrix = items.pivot(index='item_id',
                              columns='user_id',
                              values='bought').fillna(0, inplace=True)
    user_data = csr_matrix(user_matrix.values)
    user_item_matrix = user_matrix.rename_axis(None, axis=1).reset_index()
    ml_model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
    ml_model.fit(user_data)
    user_id = user_item_matrix[user_item_matrix['user_id'] == user_id].index[0]
    distances, indices = ml_model.kneighbors(user_data[user_id],
                                             n_neighbors=recommendations + 1).squeeze().tolist()
    indices_distances = list(zip(indices, distances))
    result = sorted(indices_distances, key=lambda x: x[1], reverse=False)[1:]
    return [i[0] for i in result]
