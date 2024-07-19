# Cryptocurrency Price Tracker

A simple web application to track the prices and historical data of popular cryptocurrencies using the Gemini API and CryptoCompare API. Built with Python, Streamlit, Pandas, Matplotlib, and Plotly.

## Features

- Display current price, bid price, and ask price for selected cryptocurrencies.
- Display historical data with customizable time frames.
- Interactive candlestick chart for visualizing historical price data.
- Real-time data refresh.

## Technologies Used

- Python
- Streamlit
- Requests
- Pandas
- Matplotlib
- Plotly
- Dotenv

## Setup and Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/crypto-price-tracker.git
    cd crypto-price-tracker
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables:
    - Create a `.env` file in the project directory.
    - Add your CryptoCompare API key to the `.env` file:
        ```env
        CRYPTOCOMPARE_API_KEY=your_cryptocompare_api_key
        ```

### Running the Application

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## Usage

1. Select the cryptocurrency you want to track from the sidebar (BTC, ETH, LTC, BCH, ZEC).
2. Select the time frame for historical data (1m, 5m, 15m, 30m, 1h, 6h, 1d).
3. View the current price, bid price, and ask price in the main window.
4. View the historical data table and the candlestick chart for the selected cryptocurrency and time frame.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.



## Acknowledgements

- [Streamlit](https://www.streamlit.io/)
- [CryptoCompare API](https://min-api.cryptocompare.com/)
- [Gemini API](https://docs.gemini.com/rest-api/)
- [Matplotlib](https://matplotlib.org/)
- [Plotly](https://plotly.com/python/)

