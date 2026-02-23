import numpy as np

def calculate_risk_momentum(df):

    # If predicted_severity missing, fallback to severity_index
    if "predicted_severity" not in df.columns:
        if "severity_index" in df.columns:
            df["predicted_severity"] = df["severity_index"]
        else:
            return df

    # Always create columns (even if values are small)
    df["volatility_factor"] = np.random.uniform(0.95, 1.05, len(df))

    df["risk_momentum"] = (
        df["predicted_severity"] *
        df["volatility_factor"]
    )

    df["momentum_level"] = df["risk_momentum"].apply(classify_momentum)

    return df


def classify_momentum(value):
    if value > 1.0:
        return "SURGING"
    elif value > 0.7:
        return "RISING"
    elif value > 0.4:
        return "STABLE"
    else:
        return "LOW"