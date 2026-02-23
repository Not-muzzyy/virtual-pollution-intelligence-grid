import pandas as pd
from utils.severity_index import calculate_severity_index
from utils.reliability import calculate_reliability
from utils.source_estimation import estimate_pollution_source
from utils.alert_engine import generate_alerts
from utils.urban_rural_analysis import classify_urban_rural , compare_urban_rural
from simulation.spread_simulation import simulate_spread
# Load cleaned dataset
df = pd.read_csv("data/cleaned_aqi_with_coords.csv")

# Calculate Pollution Severity Index
df_with_severity = calculate_severity_index(df)

print("\n--- Severity Index Preview ---")
print(df_with_severity[['state', 'city', 'date', 'severity_index']].head())

# Calculate Reliability Score
reliability = calculate_reliability(df)

print("\n--- Reliability Score ---")
print("Reliability Score:", reliability)

# Calculate Estimate Source
source = estimate_pollution_source(df_with_severity)

print("\n------Estimated Pollution Source Coords------")
print(source)

# Simulate Pollution Spread
spread_df = simulate_spread(df_with_severity,
source['source_longitude'], 
source['source_latitude'] )
print("\n------Spread Simulation Preview-----")
print(spread_df[['state','city','predicted_severity']].head())

# Smart alert engine 
alerts = generate_alerts(spread_df, reliability)
print("\n----- TOP ALERT PRIORITY REPORT -----")
print(alerts)

#urban vs rural comparsion
classified_df = classify_urban_rural(spread_df)
comparsion = compare_urban_rural(classified_df)
print("\n-----Urban VS Rural Pollution Comparsion")
print(comparsion)