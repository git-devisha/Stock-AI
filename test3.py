import streamlit as st
import pandas as pd
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Set up the app
st.set_page_config(page_title="Stock Prediction", layout="wide")
st.title("📈 Indian Stock/Commodity Price Predictor")
st.write("Predict future prices using historical trends")

# Sample data for Indian market (mock values as of March 2023)
STOCK_DATA = {
    "RELIANCE": {"current": 1169.50, "sector": "Oil & Gas", "volatility": 0.025},
    "TCS": {"current": 3260.55, "sector": "IT", "volatility": 0.018},
    "HDFCBANK": {"current": 1650, "sector": "Banking", "volatility": 0.022},
    "INFY": {"current": 1450, "sector": "IT", "volatility": 0.02},
    "HINDUNILVR": {"current": 2560, "sector": "FMCG", "volatility": 0.015},
    "ICICIBANK": {"current": 920, "sector": "Banking", "volatility": 0.023},
    "BANK-NIFTY": {"current": 50240.15, "sector": "Banking", "volatility": 0.02},
    "NIFTY" :{"current": 22460.30, "sector": "Index", "volatility": 0.02}
}

COMMODITY_DATA = {
    "GOLD": {"current": 92020, "unit": "per 10g", "volatility": 0.01},
    "SILVER": {"current": 91455, "unit": "per kg", "volatility": 0.015},
    "CRUDEOIL": {"current": 5125, "unit": "per barrel", "volatility": 0.03},
    "NATURALGAS": {"current": 301, "unit": "per MMBtu", "volatility": 0.04},
    "COPPER": {"current": 825, "unit": "per kg", "volatility": 0.025},
}

# Generate mock historical data
def generate_history(base_price, volatility, days=90):
    dates = pd.date_range(end=datetime.date.today(), periods=days)
    noise = np.random.normal(0, volatility, days).cumsum()
    prices = base_price * (1 + noise)
    return pd.DataFrame({"Date": dates, "Price": prices.round(2)})

# Simple ARIMA prediction
def predict_price(history, days_ahead):
    try:
        model = ARIMA(history['Price'], order=(5,1,0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=days_ahead)
        return forecast.iloc[-1]
    except:
        # Fallback to simple projection if ARIMA fails
        last_price = history['Price'].iloc[-1]
        avg_change = history['Price'].pct_change().mean()
        return last_price * (1 + avg_change * days_ahead)

# User inputs
col1, col2 = st.columns(2)

with col1:
    instrument_type = st.radio("Instrument Type", ["Stock", "Commodity"], horizontal=True)

    if instrument_type == "Stock":
        ticker = st.selectbox("Select Stock", list(STOCK_DATA.keys()))
        data = STOCK_DATA[ticker]
        st.caption(f"Sector: {data['sector']}")
    else:
        ticker = st.selectbox("Select Commodity", list(COMMODITY_DATA.keys()))
        data = COMMODITY_DATA[ticker]
        st.caption(f"Unit: {data['unit']}")

    lot_size = st.number_input("Lot/Quantity", min_value=1, value=100)

with col2:
    today = datetime.date.today()
    buy_date = st.date_input("Analysis Date", today)
    expiry_date = st.date_input("Target Date", today + relativedelta(months=1))

    if buy_date > today:
        st.warning("Analysis date is in future")
    if expiry_date <= buy_date:
        st.error("Target date must be after analysis date")

# Generate prediction when button clicked
if st.button("Generate Prediction", type="primary"):
    with st.spinner("Analyzing market trends..."):
        # Get historical data
        history = generate_history(data['current'], data['volatility'])

        # Calculate days to predict
        days_ahead = (expiry_date - buy_date).days
        if days_ahead <= 0:
            st.error("Invalid date range")
            st.stop()

        # Make prediction
        current_price = history['Price'].iloc[-1]
        predicted_price = predict_price(history, days_ahead)
        change_pct = ((predicted_price - current_price) / current_price) * 100

        # Display results
        st.success("Analysis complete!")

        # Key metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"₹{current_price:,.2f}")
        col2.metric("Predicted Price", f"₹{predicted_price:,.2f}", f"{change_pct:.2f}%")
        confidence = min(95, max(65, 100 - (data['volatility']*1000)))
        col3.metric("Confidence Level", f"{confidence:.0f}%")

        # Investment calculation
        st.subheader("Investment Scenario")
        investment = lot_size * current_price
        projected = lot_size * predicted_price
        profit = projected - investment

        col1, col2, col3 = st.columns(3)
        col1.metric("Investment Value", f"₹{investment:,.2f}")
        col2.metric("Projected Value", f"₹{projected:,.2f}")
        col3.metric("Potential P&L", f"₹{profit:,.2f}", f"{(profit/investment)*100:.2f}%")

        # Price history chart
        st.subheader(f"{ticker} Price History")
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(history['Date'], history['Price'])
        ax.axhline(current_price, color='gray', linestyle='--')
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (₹)")
        ax.grid(True)
        st.pyplot(fig)

        # Additional analysis
        st.subheader("Technical Indicators")
        history['MA_7'] = history['Price'].rolling(7).mean()
        history['MA_21'] = history['Price'].rolling(21).mean()

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(history['Date'], history['Price'], label='Price')
        ax.plot(history['Date'], history['MA_7'], label='7-day MA')
        ax.plot(history['Date'], history['MA_21'], label='21-day MA')
        ax.legend()
        ax.set_title("Moving Averages")
        st.pyplot(fig)

        # Simulate actual future price for evaluation (mocking true value)
        future_history = generate_history(current_price, data['volatility'], days=days_ahead)
        actual_future_price = future_history['Price'].iloc[-1]
        mae = abs(predicted_price - actual_future_price)
        rmse = np.sqrt((predicted_price - actual_future_price) ** 2)
        percentage_error = ((predicted_price - actual_future_price) / actual_future_price) * 100

        st.subheader("📊 Prediction Accuracy (Simulated)")
        col1, col2, col3 = st.columns(3)
        col1.metric("Actual Future Price", f"₹{actual_future_price:,.2f}")
        col2.metric("MAE", f"₹{mae:,.2f}")
        col3.metric("RMSE", f"₹{rmse:,.2f}")
        # st.metric("Percentage Error", f"{percentage_error:.2f}%", delta_color="inverse")

# Disclaimer
st.markdown("---")
st.warning("""
**Note:** This is a simulation using mock data and statistical models. 
Actual market behavior may differ significantly. The predictions shown are 
for educational purposes only and should not be considered as investment advice.
""")

# How it works section
with st.expander("How this prediction works"):
    st.markdown("""
    This app uses:
    - **ARIMA model** for time series forecasting
    - **Technical indicators** like moving averages
    - **Volatility-adjusted** projections based on sector trends

    The simulation:
    1. Generates realistic historical price data
    2. Analyzes trends and patterns
    3. Projects future prices based on statistical models

    For more accurate predictions, you would need:
    - Real-time market data feeds
    - Fundamental analysis inputs
    - News sentiment integration
    """)
