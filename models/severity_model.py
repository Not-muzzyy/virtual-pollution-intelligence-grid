import pandas as pd

def calculate_severity_index(df):
    """
    Calculate normalized pollution severity index
    using PM2.5, PM10, NO2 weighted scoring.
    """

    df = df.copy()

    # Normalize pollutants
    df["pm25_norm"] = df["PM2.5"] / df["PM2.5"].max()
    df["pm10_norm"] = df["PM10"] / df["PM10"].max()
    df["no2_norm"] = df["NO2"] / df["NO2"].max()

    # Weighted severity score
    df["severity_index"] = (
        0.5 * df["pm25_norm"] +
        0.3 * df["pm10_norm"] +
        0.2 * df["no2_norm"]
    )

    return df