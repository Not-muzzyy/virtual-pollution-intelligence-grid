import streamlit as st
import pandas as pd
import folium
import plotly.express as px
from streamlit_folium import st_folium

# Backend imports
from utils.severity_index import calculate_severity_index
from utils.reliability import calculate_reliability
from utils.source_estimation import estimate_pollution_source
from simulation.spread_simulation import simulate_spread
from utils.alert_engine import generate_alerts
from utils.urban_rural_analysis import classify_urban_rural, compare_urban_rural
from backend.risk_momentum import calculate_risk_momentum
from backend.impact_projection import project_7day_impact
from models.severity_model import calculate_severity_index
from models.risk_model import calculate_risk_score
from models.forecast_model import forecast_7_day_trend

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(page_title="Virtual Pollution Intelligence Grid", layout="wide",initial_sidebar_state="expanded")
st.markdown("""
<style>
[data-testid="stMetric"] {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
st.title("🌍 Virtual Pollution Intelligence Grid")
st.markdown("AI-driven Environmental Risk Forecasting System") 
st.divider()


# ==========================
# LOAD DATA
# ==========================
df = pd.read_csv("data/cleaned_aqi_with_coords.csv")


# ==========================
# CONTROL PANEL
# ==========================
st.sidebar.markdown("### ⚙ Control Panel")
st.sidebar.markdown("### 🌬 Wind Simulation")

wind_direction = st.sidebar.slider(
    "Wind Direction (Degrees)",
    min_value=0,
    max_value=360,
    value=90
)

wind_strength = st.sidebar.slider(
    "Wind Strength",
    min_value=0.0,
    max_value=1.0,
    value=0.3,
    step=0.1
)
st.sidebar.divider()

st.sidebar.markdown("### Scenario Simulation")

scenario = st.sidebar.selectbox(
    "Select Environmental Scenario",
    [
        "Normal Conditions",
        "Industrial Surge (+30%)",
        "High Wind Spread",
        "Emergency Containment"
    ]
)
st.sidebar.divider()
col1, col2 = st.columns(2)

with col1:
    selected_state = st.selectbox(
        "Select State",
        options=["All"] + sorted(df["state"].unique())
    )

with col2:
    spread_intensity = st.slider(
        "Spread Intensity Factor",
        0.05, 0.50, 0.20, 0.05
    )

if selected_state != "All":
    df = df[df["state"] == selected_state]

st.divider()


# ==========================
# CORE PROCESSING PIPELINE
# ==========================
df = calculate_severity_index(df)
df = forecast_7_day_trend(df)
df = calculate_risk_score(df)
reliability = calculate_reliability(df)

source = estimate_pollution_source(df)

if (
    source is None or
    source.get("source_latitude") is None or
    source.get("source_longitude") is None
):
    st.warning("Not enough valid data for this selection.")
    st.stop()

# Spread Simulation
df = simulate_spread(
    df,
    source["source_latitude"],
    source["source_longitude"],
    intensity_factor=0.2,
    wind_direction=wind_direction,
    wind_strength=wind_strength
)
# Apply Scenario Impact
if scenario == "Industrial Surge (+30%)":
    df["predicted_severity"] *= 1.3

elif scenario == "High Wind Spread":
    df["predicted_severity"] *= 1.2

elif scenario == "Emergency Containment":
    df["predicted_severity"] *= 0.7
    # Severity Classification
def classify_severity(sev):
    if sev > 0.8:
        return "CRITICAL"
    elif sev > 0.6:
        return "HIGH"
    elif sev > 0.4:
        return "MODERATE"
    else:
        return "LOW"

df["severity_label"] = df["predicted_severity"].apply(classify_severity)
# Risk Momentum
df = calculate_risk_momentum(df)

# 7-Day Projection
df = project_7day_impact(df)

# Alerts
alerts = generate_alerts(df, reliability)

# Urban vs Rural
classified = classify_urban_rural(df)
comparison = compare_urban_rural(classified)


# =========================
# EXECUTIVE SUMMARY
# =========================

st.divider()
st.subheader("📊 Executive Intelligence Overview")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

if not df.empty:

    # Reliability
    with col1:
        st.metric("🧠 Model Reliability", round(reliability, 3))

    # Highest Severity City
    highest = df.sort_values("predicted_severity", ascending=False).iloc[0]
    with col2:
        st.metric(
            "🔥 Highest Risk City",
            highest["city"],
            delta=round(highest["predicted_severity"], 2)
        )

    # Average Severity
    with col3:
        st.metric(
            "🌫 Avg Severity",
            round(df["predicted_severity"].mean(), 3)
        )

    # Total Cities
    with col4:
        st.metric(
            "🏙 Cities Analyzed",
            len(df)
        )

st.divider()
# ==========================
# MAP SECTION
# ==========================
st.divider()
st.subheader("🗺 Geographic Spread Intelligence System")
st.caption("Live simulation of pollution dispersion based on modeled severity and inferred source dynamics.")
st.markdown("<br>", unsafe_allow_html=True)

map_col1, map_col2 = st.columns([3, 1])

m = folium.Map(location=[20.5, 78.9], zoom_start=5)

def get_color(severity):
    if severity > 1.0:
        return "darkred"
    elif severity > 0.7:
        return "red"
    elif severity > 0.4:
        return "orange"
    else:
        return "green"
# 🔥 Highlight estimated pollution source
folium.Marker(
    location=[source["source_latitude"], source["source_longitude"]],
    popup="🔥 Estimated Pollution Source",
    icon=folium.Icon(color="red", icon="fire")
).add_to(m)

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
      radius=5 + (row["predicted_severity"] * 15),
       popup=f"""
City: {row['city']}  
State: {row['state']}  
Severity: {round(row['predicted_severity'], 2)}
""",
        color=get_color(row["predicted_severity"]),
        fill=True
    ).add_to(m)

folium.Marker(
    location=[source["source_latitude"], source["source_longitude"]],
    popup="Estimated Pollution Source",
    icon=folium.Icon(color="blue")
).add_to(m)

with map_col1:
    st_folium(m, width=1000, height=500)

with map_col2:
    st.markdown("### 🧭 Source Info")
    st.write(f"Latitude: {round(source['source_latitude'], 4)}")
    st.write(f"Longitude: {round(source['source_longitude'], 4)}")
    st.write(f"Spread Intensity: {spread_intensity}")
st.divider()


# ==========================
# ADVANCED RISK MODELS
# ==========================
st.subheader("📊 Advanced Risk Models")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📈 Risk Momentum")
    if "risk_momentum" in df.columns:
        st.dataframe(
            df[["state", "city", "risk_momentum", "momentum_level"]]
            .sort_values("risk_momentum", ascending=False)
            .head(10),
            use_container_width=True
        )

with col2:
    st.markdown("### 🔮 7-Day Impact Projection")
    if "projected_7day_severity" in df.columns:
        st.dataframe(
            df[["state", "city", "projected_7day_severity", "projected_alert"]]
            .sort_values("projected_7day_severity", ascending=False)
            .head(10),
            use_container_width=True
        )

st.divider()


# ==========================
# ALERT PRIORITY SECTION
# ==========================``
st.subheader("🚨 Priority Alert System")

st.dataframe(alerts.head(10), use_container_width=True,height=300)

st.divider()


# ==========================
# URBAN VS RURAL (PROFESSIONAL CHART)
# ==========================
st.subheader("🏙 Urban vs Rural Impact Distribution")
if "area_type" not in df.columns:
    severity_threshold = df["predicted_severity"].median()

    df["area_type"] = df["predicted_severity"].apply(
        lambda x: "Urban" if x >= severity_threshold else "Rural"
    )
area_avg = df.groupby("area_type")["predicted_severity"].mean().reset_index()

import plotly.graph_objects as go

fig = go.Figure(data=[go.Pie(
    labels=area_avg["area_type"],
    values=area_avg["predicted_severity"],
    hole=0.2
)])

fig.update_traces(
    textinfo='label+percent',
    pull=[0.05, 0.05]
)

fig.update_layout(
    title="Average Predicted Severity Share",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font=dict(color="white"),
)

st.plotly_chart(fig, use_container_width=True)
    
st.divider()
st.caption("Virtual Pollution Intelligence Grid • AI-driven Simulation Model • 24-Hour Hackathon Prototype")