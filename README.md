# Stock-AI

# Monte Carlo Price Predictor
## Overview
Monte Carlo Price Predictor is a Streamlit web application that simulates future price predictions using Monte Carlo methods. The app generates random price movements based on specified volatility parameters and predicts potential future values. This tool is helpful for understanding potential price movements and the effects of volatility on financial instruments.

## Features
- Simulate historical price data based on volatility parameters
- Predict future prices using Monte Carlo simulations
- Visualize historical price movements
- Compare predicted prices with simulated actual outcomes
- Calculate prediction accuracy metrics (MAE, RMSE, Percentage Error)

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup
1. Clone this repository or download the source code
2. Install the required dependencies:
```bash
pip install streamlit numpy pandas
```

## Usage
1. Run the application:
```bash
streamlit run test3.py
```
2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)
3. Configure the parameters:
   - Initial Price (₹): The starting price value
   - Volatility: The standard deviation of price movements
   - Days Ahead to Predict: Number of days into the future to predict
4. Click "Predict Future Price 🔮" to generate the prediction

## How It Works
1. The app uses a stochastic process to simulate price histories
2. Each day's price is calculated based on the previous day's price plus a random shock
3. The shock is sampled from a normal distribution with mean 0 and standard deviation equal to the volatility parameter
4. For prediction accuracy estimation, the app compares the predicted price with a simulated "actual" future price

## Metrics Explanation
- **MAE (Mean Absolute Error)**: Measures the average magnitude of errors in the prediction
- **RMSE (Root Mean Square Error)**: Measures the square root of the average squared differences between predicted and actual values
- **Percentage Error**: The percentage difference between the predicted and actual prices

## Limitations
- This is a simplified model that assumes normal distribution of price changes
- Real financial instruments may have more complex behaviors
- The simulated "actual" values are generated using the same model as the prediction

## Future Improvements
- Add multiple simulation runs to generate a distribution of potential outcomes
- Include different statistical models for price prediction
- Add additional visualization options (histograms, box plots, etc.)
- Implement parameter optimization based on historical data
