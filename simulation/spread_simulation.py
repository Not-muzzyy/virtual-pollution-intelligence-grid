import numpy as np
import pandas as pd


def simulate_spread(df, source_lat, source_lon,
                    intensity_factor=0.2,
                    wind_direction=0,
                    wind_strength=0.0):

    df = df.copy()

    if source_lat is None or source_lon is None:
        df["spread_impact"] = 0
        df["distance_from_source"] = 0
        return df

    # Step 1: Distance calculation
    df["distance_from_source"] = np.sqrt(
        (df["latitude"] - source_lat) ** 2 +
        (df["longitude"] - source_lon) ** 2
    )

    df["distance_from_source"] = df["distance_from_source"].replace(0, 0.0001)

    # Step 2: Base inverse distance impact
    base_spread = intensity_factor * (
        1 / df["distance_from_source"]
    )

    # Step 3: Wind directional influence
    # Convert wind direction to radians
    wind_rad = np.radians(wind_direction)

    # Compute angle between source and each city
    delta_lat = df["latitude"] - source_lat
    delta_lon = df["longitude"] - source_lon

    city_angle = np.arctan2(delta_lat, delta_lon)

    # Wind alignment factor (cosine similarity)
    wind_alignment = np.cos(city_angle - wind_rad)

    # Normalize alignment (keep only positive influence)
    wind_alignment = wind_alignment.clip(lower=0)

    # Apply wind strength
    wind_effect = wind_strength * wind_alignment

    # Final spread impact
    df["spread_impact"] = base_spread * (1 + wind_effect)

    # Final predicted severity
    df["predicted_severity"] = (
        df["severity_index"] + df["spread_impact"]
    )

    return df