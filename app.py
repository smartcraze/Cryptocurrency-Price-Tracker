import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
CRYPTOCOMPARE_API_KEY = os.getenv("CRYPTOCOMPARE_API_KEY")
GEMINI_API_URL = "https://api.gemini.com/v1"

def get_ticker_price(symbol):
    response = requests.get(f"{GEMINI_API_URL}/pubticker/{symbol}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error(f"Error fetching ticker price: {response.status_code}")
        return None

def get_historical_data(symbol, time_frame):
    time_frame_map = {
        "1m": "minute",
        "5m": "minute",
        "15m": "minute",
        "30m": "minute",
        "1h": "hour",
        "6h": "hour",
        "1d": "day"
    }
    limit = {
        "1m": 60,
        "5m": 60,
        "15m": 60,
        "30m": 60,
        "1h": 24,
        "6h": 24,
        "1d": 30
    }[time_frame]

    response = requests.get(
        f"https://min-api.cryptocompare.com/data/v2/histo{time_frame_map[time_frame]}",
        params={
            "fsym": symbol.upper(),
            "tsym": "USD",
            "limit": limit,
            "api_key": CRYPTOCOMPARE_API_KEY
        }
    )
    if response.status_code == 200:
        data = response.json()["Data"]["Data"]
        df = pd.DataFrame(data)
        df["time"] = pd.to_datetime(df["time"], unit="s")
        return df
    else:
        st.error(f"Error fetching historical data: {response.status_code}")
        return pd.DataFrame()

def main():
    st.title("Cryptocurrency Price Tracker")
    
    st.sidebar.title("Settings")
    symbol = st.sidebar.selectbox("Select Cryptocurrency", ["BTC", "ETH", "LTC", "BCH", "ZEC"])
    time_frame = st.sidebar.selectbox("Select Time Frame", ["1m", "5m", "15m", "30m", "1h", "6h", "1d"])
    
    st.header(f"Price for {symbol.upper()}")
    
    data = get_ticker_price(f"{symbol.lower()}usd")
    
    if data:
        st.write(f"**Last Price:** ${data['last']}")
        st.write(f"**Bid Price:** ${data['bid']}")
        st.write(f"**Ask Price:** ${data['ask']}")
    else:
        st.write("Failed to fetch data.")
    
    st.header(f"Historical Data for {symbol.upper()} ({time_frame})")
    
    historical_data = get_historical_data(symbol, time_frame)
    
    if not historical_data.empty:
        st.write(historical_data)
        
        fig, ax = plt.subplots()
        ax.plot(historical_data["time"], historical_data["close"], label="Close Price")
        ax.set_xlabel("Time")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)

        # Plot candlestick chart with Plotly
        fig_candlestick = go.Figure(data=[go.Candlestick(
            x=historical_data['time'],
            open=historical_data['open'],
            high=historical_data['high'],
            low=historical_data['low'],
            close=historical_data['close']
        )])
        fig_candlestick.update_layout(
            title=f"Candlestick Chart for {symbol.upper()}",
            xaxis_title="Time",
            yaxis_title="Price",
        )
        st.plotly_chart(fig_candlestick)
    else:
        st.write("Failed to fetch historical data.")
    
    if st.sidebar.button("Refresh"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
