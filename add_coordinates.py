import pandas as pd

# Load original raw dataset
raw_df = pd.read_csv("data/AQI.csv")

# Keep only needed columns
raw_coords = raw_df[['state', 'city', 'latitude', 'longitude']]

# Drop duplicates (one lat/long per city)
raw_coords = raw_coords.drop_duplicates(subset=['state', 'city'])

# Load cleaned dataset
cleaned_df = pd.read_csv("data/cleaned_aqi_data.csv")

# Merge coordinates into cleaned data
merged_df = pd.merge(
    cleaned_df,
    raw_coords,
    on=['state', 'city'],
    how='left'
)

# Save updated file
merged_df.to_csv("data/cleaned_aqi_with_coords.csv", index=False)

print("✅ Coordinates added successfully.")
print("New Shape:", merged_df.shape)
print(merged_df[['state', 'city', 'latitude', 'longitude']].head())