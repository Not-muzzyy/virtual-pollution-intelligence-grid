import pandas as pd

def normalize_column(series):
    """Min-Max normalization"""
    return (series - series.min()) / (series.max() - series.min())

def calculate_severity_index(df):
    """
    Takes dataframe with PM2.5, PM10, NO2
    Returns dataframe with new column: severity_index
    """

    df = df.copy()

    # Normalize pollutants
    df['PM2.5_norm'] = normalize_column(df['PM2.5'])
    df['PM10_norm'] = normalize_column(df['PM10'])
    df['NO2_norm'] = normalize_column(df['NO2'])

    # Weighted Severity Formula
    df['severity_index'] = (
        0.6 * df['PM2.5_norm'] +
        0.3 * df['PM10_norm'] +
        0.1 * df['NO2_norm']
    )

    return df