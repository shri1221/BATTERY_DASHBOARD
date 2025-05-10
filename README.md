# 🔋 Battery Telemetry Dashboard

This is an interactive dashboard built with **Streamlit** for visualizing battery telemetry data (SOC, voltage, temperature) from a BMS (Battery Management System).

## 📊 Features

- Summary of key battery metrics (SOC, voltage, temperature)
- Interactive line charts for:
  - State of Charge (SOC)
  - Max/Min Voltage
  - Max/Min Temperature
  - Combined view
- Raw data viewer

## 📁 Files

- `app.py` – Main Streamlit app
- `BMS.xlsx` – Sample battery data
- `requirements.txt` – Python dependencies

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/battery-dashboard.git
cd battery-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
