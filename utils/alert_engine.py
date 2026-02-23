import pandas as pd

def generate_alerts(df, reliability_score):
    """
    Generates smart priority alerts
    """

    df = df.copy()

    # Base severity factor
    df['risk_score'] = df['predicted_severity']

    # Reliability multiplier
    df['risk_score'] = df['risk_score'] * (1 + (1 - reliability_score))

    # Assign alert category
    def categorize(score):
        if score >= 0.75:
            return "CRITICAL"
        elif score >= 0.5:
            return "HIGH"
        elif score >= 0.3:
            return "MODERATE"
        else:
            return "LOW"

    df['alert_level'] = df['risk_score'].apply(categorize)

    # Rank by highest risk
    df = df.sort_values(by='risk_score', ascending=False)

    return df[['state', 'city', 'risk_score', 'alert_level']].head(10)