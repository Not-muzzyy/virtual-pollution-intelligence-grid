def calculate_risk_score(df):
    """
    Combine severity and spread impact
    to calculate final risk score.
    """

    df = df.copy()

    if "spread_impact" in df.columns:
        df["risk_score"] = df["severity_index"] + df["spread_impact"]
    else:
        df["risk_score"] = df["severity_index"]

    # Assign alert levels
    def classify_risk(score):
        if score > 1.0:
            return "CRITICAL"
        elif score > 0.7:
            return "HIGH"
        elif score > 0.4:
            return "MODERATE"
        else:
            return "LOW"

    df["alert_level"] = df["risk_score"].apply(classify_risk)

    return df