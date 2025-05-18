

# AIDRoute: AI-Powered Disaster Relief System

**Course:** Statistics with AI (TCS-IV-T095)
**Team:** RapidRelief Squad

---

## Overview

AIDRoute is an AI-augmented disaster relief routing system designed for the Uttarakhand region. It integrates real-time weather data, forecasts road risks, prioritizes aid zones using multi-criteria decision analysis (MCDA), and provides NGO-ready visualizations and reports.

---

## Features

- **Real-time rain and hazard data** integration using Open-Meteo API (no API key required)
- **Road risk forecasting** using ARIMA time-series and Bayesian updates
- **Zone prioritization** based on urgency, population, and demand (MCDA approach)
- **Safe and dynamic routing** using weighted graph shortest paths (NetworkX & Dijkstra)
- **Interactive Folium map** with color-coded safe routes and zones
- **Excel report**, **PowerPoint presentation**, and **demand charts** for NGO use
- **Streamlit dashboard** for live data upload and output visualization
- **Fallback system** to use offline data if API unavailable

---

## Folder Structure

```plaintext
AIDRoute/
├── data/
│   ├── roads.csv            # Road network data
│   ├── zone_demand.csv      # Zone-wise urgency and population
│   └── live_updates.json    # Real-time hazard data (updated dynamically)
├── core/
│   ├── data_loader.py       # Data loading and API integration
│   ├── risk_model.py        # Road risk forecasting logic
│   ├── demand_scoring.py    # MCDA zone scoring logic
│   ├── router.py            # Graph building and routing
│   └── report_generator.py  # Excel, chart, and PPT generation
├── ui/
│   ├── map_visualizer.py    # Folium map generation
│   └── streamlit_app.py     # Interactive NGO dashboard
├── run_pipeline.py          # Main pipeline runner script
├── requirements.txt         # Python dependencies
└── README.md                # This file
```
