import pandas as pd

def classify_urban_rural(df):
    """
    Simple classification logic:
    Cities containing 'Nagar', 'Puram', 'Patti' treated as semi/rural
    Major known metros treated as Urban
    """

    urban_keywords = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bengaluru', 'Hyderabad', 'Pune', 'Ahmedabad']

    df = df.copy()

    def classify(city):
        for metro in urban_keywords:
            if metro.lower() in city.lower():
                return "Urban"
        return "Rural"

    df['area_type'] = df['city'].apply(classify)

    return df


def compare_urban_rural(df):
    """
    Compare predicted severity between Urban and Rural
    """

    summary = df.groupby('area_type')['predicted_severity'].mean().reset_index()

    summary = summary.sort_values(by='predicted_severity', ascending=False)

    return summary