import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_excel(r"C:\Users\HP\Desktop\BMS.xlsx")

# Clean unnamed or empty column
if ' ' in df.columns:
    df = df.drop(columns=[' '])

# Rename columns for clarity
df.rename(columns={
    'MaxCellV[V]': 'MAX_VOLTAGE',
    'MinCellV[V]':'MIN_VOLTAGE',
    'SOC_%': 'SOC',
    'v003_HEV_CAN_DBC_BMU::B2V_BMSValue7::B2V_MaxCellT[°C]': 'MaxTemp',
    'v003_HEV_CAN_DBC_BMU::B2V_BMSValue7::B2V_MinCellT[°C]': 'MinTemp',
    'DATE_TIME': 'TIME'
}, inplace=True)

# Ensure TIME column is in datetime format
df['TIME'] = pd.to_datetime(df['TIME'])

# Streamlit UI
st.set_page_config(page_title="Battery Monitoring Dashboard", layout="wide")
st.title("🔋 Battery Telemetry Dashboard")

# Summary metrics
st.subheader("📊 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Max SOC (%)", f"{df['SOC'].max():.2f}")
col2.metric("Max Voltage (V)", f"{df['MAX_VOLTAGE'].max():.2f}")
col3.metric("Max Temperature (°C)", f"{df['MaxTemp'].max():.2f}")

col4, col5 = st.columns(2)
col4.metric("Min Voltage (V)", f"{df['MIN_VOLTAGE'].min():.2f}")
col5.metric("Min Temperature (°C)", f"{df['MinTemp'].min():.2f}")

# Interactive Line Charts
st.subheader("📈 Trend Analysis")

tab1, tab2, tab3, tab4 = st.tabs(["SOC Over Time", "Voltage Over Time", "Temperature Over Time", "All in One"])

with tab1:
    fig_soc = px.line(df, x='TIME', y='SOC', title="State of Charge (%) Over Time")
    st.plotly_chart(fig_soc, use_container_width=True)

with tab2:
    # Updated: Show Max Voltage and Min Voltage in one graph
    fig_volt = px.line(df, x='TIME', y=['MAX_VOLTAGE', 'MIN_VOLTAGE'], 
                       title="Max vs Min Voltage Over Time",
                       labels={'value': 'Voltage (V)', 'TIME': 'Time'},
                       color_discrete_map={"MAX_VOLTAGE": "red", "MIN_VOLTAGE": "blue"})
    st.plotly_chart(fig_volt, use_container_width=True)

with tab3:
    fig_temp = px.line(df, x='TIME', y=['MaxTemp', 'MinTemp'], title="Cell Temperature (°C) Over Time")
    st.plotly_chart(fig_temp, use_container_width=True)

with tab4:
    # Correct the column name 'Voltage' to 'MAX_VOLTAGE' for the all-in-one graph
    fig_all = px.line(df, x='TIME', y=['SOC', 'MAX_VOLTAGE', 'MaxTemp','MIN_VOLTAGE'], title="SOC, Voltage, and MaxTemp Trends")
    st.plotly_chart(fig_all, use_container_width=True)


# Show raw data
with st.expander("📄 View Raw Data"):
    st.dataframe(df)
