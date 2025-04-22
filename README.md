# 📈 Stock-AI

**Stock-AI** is an interactive Streamlit web application that simulates future stock price movements using Monte Carlo methods. It allows users to visualize potential future price trajectories based on historical volatility, providing insights into the effects of market fluctuations on financial instruments.

## 🚀 Features

- **Historical Data Simulation**: Generate synthetic historical price data based on user-defined volatility parameters.
- **Monte Carlo Forecasting**: Predict future stock prices through Monte Carlo simulations.
- **Interactive Visualizations**: Visualize both historical and predicted price movements.
- **Accuracy Metrics**: Evaluate prediction accuracy using metrics like MAE (Mean Absolute Error), RMSE (Root Mean Square Error), and Percentage Error.

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/git-devisha/Stock-AI.git
   cd Stock-AI
   ```

2. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   *Alternatively, install packages individually:*

   ```bash
   pip install streamlit numpy pandas
   ```

## 💻 Usage

1. **Run the Application**

   ```bash
   streamlit run test3.py
   ```

2. **Access the Web Interface**

   After running the above command, Streamlit will provide a local URL (typically `http://localhost:8501`). Open this URL in your web browser to interact with the application.

## 📂 Project Structure

```
Stock-AI/
├── test3.py             # Main Streamlit application script
├── requirements.txt     # List of required Python packages
└── README.md            # Project documentation
```

## 📊 Example Output

*Note: Include screenshots or GIFs here to showcase the application's interface and features.*

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance the application, fix bugs, or add new features:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request detailing your changes.
