import pandas as pd

# ==========================
# STEP 1 — Load Dataset
# ==========================
print("Loading dataset...")
df = pd.read_csv("AQI.csv")

print("Original Shape:", df.shape)
print("Columns:", df.columns)
print("\nUnique Pollutants:")
print(df['pollutant_id'].unique())


# ==========================
# STEP 2 — Keep Only Required Pollutants
# ==========================
required_pollutants = ['PM2.5', 'PM10', 'NO2']

df_filtered = df[df['pollutant_id'].isin(required_pollutants)]

print("\nAfter Filtering Shape:", df_filtered.shape)
print("Remaining Pollutants:", df_filtered['pollutant_id'].unique())


# ==========================
# STEP 3 — Convert Date
# ==========================
print("\nConverting date column...")

df_filtered['last_update'] = pd.to_datetime(df_filtered['last_update'], errors='coerce')
df_filtered['date'] = df_filtered['last_update'].dt.date

# Remove rows where date conversion failed
df_filtered = df_filtered.dropna(subset=['date'])


# ==========================
# STEP 4 — Pivot (Long → Wide)
# ==========================
print("\nPivoting dataset...")

df_pivot = df_filtered.pivot_table(
    index=['state', 'city', 'date'],
    columns='pollutant_id',
    values='pollutant_avg'
).reset_index()

print("Pivoted Shape:", df_pivot.shape)
print(df_pivot.head())


# ==========================
# STEP 5 — Handle Missing Values
# ==========================
print("\nChecking missing values...")
print(df_pivot.isnull().sum())

# Fill missing pollutant values with median
df_pivot['PM2.5'] = df_pivot['PM2.5'].fillna(df_pivot['PM2.5'].median())
df_pivot['PM10'] = df_pivot['PM10'].fillna(df_pivot['PM10'].median())
df_pivot['NO2'] = df_pivot['NO2'].fillna(df_pivot['NO2'].median())


# ==========================
# STEP 6 — Final Check
# ==========================
print("\nFinal Dataset Info:")
print(df_pivot.info())
print(df_pivot.head())


# ==========================
# STEP 7 — Save Clean File
# ==========================
df_pivot.to_csv("cleaned_aqi_data.csv", index=False)

print("\n✅ Cleaned file saved as: cleaned_aqi_data.csv")