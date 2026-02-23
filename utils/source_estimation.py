import pandas as pd
from sklearn.cluster import KMeans

def estimate_pollution_source(df):

    if 'latitude' not in df.columns or 'longitude' not in df.columns:
        raise ValueError("Latitude and Longitude columns are required")

    data = df[['latitude', 'longitude', 'severity_index']].dropna()

    # CASE 1: No data at all
    if len(data) == 0:
        return {
            "source_latitude": None,
            "source_longitude": None
        }

    # CASE 2: Too few rows for clustering
    if len(data) < 3:
        max_row = data.loc[data['severity_index'].idxmax()]
        return {
            "source_latitude": round(max_row['latitude'], 5),
            "source_longitude": round(max_row['longitude'], 5)
        }

    # CASE 3: Normal clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    data['cluster'] = kmeans.fit_predict(data[['latitude', 'longitude']])

    cluster_severity = data.groupby('cluster')['severity_index'].mean()
    highest_cluster = cluster_severity.idxmax()

    centroid = kmeans.cluster_centers_[highest_cluster]

    return {
        "source_latitude": round(centroid[0], 5),
        "source_longitude": round(centroid[1], 5)
    }