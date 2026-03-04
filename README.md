# 🌍 Virtual Pollution Intelligence Grid

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/AI-Environmental%20Intelligence-green?style=for-the-badge&logo=leaflet&logoColor=white"/>
  <img src="https://img.shields.io/badge/Built%20At-Chakravyuha%203.0%20Hackathon-ff69b4?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  An AI-powered environmental risk forecasting and anomaly detection system — built in 24 hours at Chakravyuha 3.0, BITM Bellary.
</p>

-----

## 🏆 Hackathon Context

This project was built during **Chakravyuha 3.0** — a 24-hour hackathon organized at **BITM Bellary**. The challenge was to build a smart, software-only environmental monitoring system without relying on physical sensor hardware.

The result: a fully working AI platform that simulates, forecasts, and visualizes pollution risk across Indian cities — in real time.

-----

## 🔍 What is This?

Air pollution is one of the biggest public health crises in India. Traditional monitoring requires expensive hardware sensor networks. This system solves that by using **AI + real pollution datasets** to:

- Simulate how pollution spreads across cities
- Forecast 7-day pollution trends
- Detect dangerous anomalies automatically
- Generate high-alert reports for decision makers

> 🎯 **Designed for:** Smart Cities, Climate Resilience, and Environmental Risk Intelligence systems

-----

## ✨ Key Features

|Feature                       |Description                                          |
|------------------------------|-----------------------------------------------------|
|🧪 **Composite Severity Index**|Normalized & weighted scoring across PM2.5, PM10, NO2|
|🌬️ **Scenario Simulations**    |Industrial Surge, Wind Spread, Containment scenarios |
|🗺️ **Spatial Spread Modeling** |Geographic pollution diffusion across regions        |
|📈 **7-Day Forecast**          |ML-powered trend projection                          |
|🚨 **Anomaly Detection**       |Statistical detection using Mean + 1.5σ threshold    |
|🏆 **Risk Priority Ranking**   |Ranks cities by pollution risk level                 |
|📋 **Auto Report Generation**  |Dynamic high-alert reports for decision support      |
|📊 **Interactive Dashboard**   |Live maps, charts, and analytics via Streamlit       |

-----

## 🧠 Technical Approach

```
Raw Pollution Data (PM2.5, PM10, NO2)
          │
          ▼
  Feature Normalization & Cleaning
          │
          ▼
  Weighted Composite Index Modeling
          │
     ┌────┴────┐
     ▼         ▼
Spatial      Forecast
Diffusion    Projection
Simulation   (7-Day)
     │         │
     └────┬────┘
          ▼
  Statistical Anomaly Detection
          │
          ▼
  Risk Prioritization & Scoring
          │
          ▼
  Interactive Dashboard + Alert Reports
```

-----

## 🗂️ Project Structure

```
virtual-pollution-intelligence-grid/
│
├── backend/                    → Data processing & API logic
├── data/                       → Pollution datasets (PM2.5, PM10, NO2)
├── models/                     → ML forecasting models
├── simulation/                 → Scenario simulation engines
├── utils/                      → Helper functions
├── dashboard.py                → Main Streamlit dashboard (run this)
├── clean_aqi.py                → Data cleaning pipeline
├── add_coordinates.py          → Geospatial coordinate processing
├── test_severity.py            → Severity scoring tests
└── requirements.txt            → Project dependencies
```

-----

## 🛠️ Tech Stack

|Technology    |Purpose                 |
|--------------|------------------------|
|Python        |Core language           |
|Streamlit     |Interactive dashboard   |
|Pandas & NumPy|Data processing         |
|Plotly        |Charts & visualizations |
|Folium        |Geographic map rendering|
|Scikit-learn  |ML models & forecasting |

-----

## 📦 Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/Not-muzzyy/virtual-pollution-intelligence-grid.git
cd virtual-pollution-intelligence-grid

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the dashboard
streamlit run dashboard.py
```

The dashboard will open in your browser automatically at `http://localhost:8501`

-----

## 🎯 Real-World Use Cases

- 🏙️ **Smart City Platforms** — monitor and respond to pollution spikes
- 🏥 **Public Health Departments** — early warning for vulnerable populations
- 🌱 **Climate Resilience Planning** — long-term environmental risk modeling
- 🏭 **Industrial Compliance** — track pollution impact from industrial zones
- 🔬 **Research & Policy** — data-driven environmental decision support

-----

## 🔮 Future Improvements

- [ ] Deploy live on Streamlit Cloud
- [ ] Integrate real-time AQI API feeds
- [ ] Add predictive ML model for 30-day forecasts
- [ ] Mobile-responsive dashboard
- [ ] Alert notification system (email/SMS)
- [ ] Multi-country dataset support

-----

## 👨‍💻 About the Author

**Mohammed Muzamil C**
Final Year BCA Student | Cybersecurity & Machine Learning Enthusiast
Nandi Institute of Management & Science College, Ballari
Vijayanagara Sri Krishnadevaraya University

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/muzzammilc7)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/Not-muzzyy)

-----

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

-----

<p align="center">
  ⭐ If you found this useful, please star the repository!
</p>
