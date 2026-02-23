def forecast_7_day_trend(df, growth_factor=0.05):
    """
    Simulate 7-day severity growth projection.
    """

    df = df.copy()

    df["projected_7day_severity"] = (
        df["severity_index"] * (1 + growth_factor)
    )

    return df