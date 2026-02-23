import pandas as pd
import numpy as np

def calculate_reliability(df):
    """
    Returns overall reliability score (0 to 1)
    """

    # 1️⃣ Data Completeness
    total_cells = df[['PM2.5', 'PM10', 'NO2']].size
    missing_cells = df[['PM2.5', 'PM10', 'NO2']].isnull().sum().sum()
    completeness_score = 1 - (missing_cells / total_cells)

    # 2️⃣ Stability Score (lower variance = more stable)
    variance_pm25 = np.var(df['PM2.5'])
    variance_pm10 = np.var(df['PM10'])
    variance_no2 = np.var(df['NO2'])

    avg_variance = (variance_pm25 + variance_pm10 + variance_no2) / 3

    # Convert variance to stability (simple inverse scaling)
    stability_score = 1 / (1 + avg_variance)

    # Final weighted score
    reliability_score = (0.7 * completeness_score) + (0.3 * stability_score)

    return round(reliability_score, 4)