import numpy as np

def project_7day_impact(df):

    if "risk_momentum" not in df.columns:
        return df

    # Simulated daily growth rate
    daily_growth = 0.03  # 3% compounding

    df["projected_7day_severity"] = (
        df["risk_momentum"] *
        ((1 + daily_growth) ** 7)
    )

    df["projected_alert"] = df["projected_7day_severity"].apply(classify_projection)

    return df


def classify_projection(value):
    if value > 1.2:
        return "EXTREME"
    elif value > 0.9:
        return "VERY HIGH"
    elif value > 0.6:
        return "HIGH"
    else:
        return "MODERATE"