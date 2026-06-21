# 📈 Stock Market Anomaly Detection

An interactive Streamlit dashboard for detecting unusual stock market behavior using statistical analysis and time-series forecasting techniques.

The project analyzes historical stock prices of major NSE companies, identifies anomalous price movements using Z-score based detection, performs statistical tests, studies inter-stock correlations, and forecasts future prices using ARIMA models.

---

## 🚀 Features

- 📊 Interactive dashboard built with Streamlit
- 📈 Stock price visualization with anomaly markers
- 🔍 Z-score based anomaly detection
- 📉 20-day rolling volatility analysis
- 📋 Table of detected anomalies
- 📊 Return distribution visualization
- 🧪 Statistical tests:
  - Augmented Dickey-Fuller (ADF)
  - Jarque-Bera Test
  - Shapiro-Wilk Test
- 🔗 Correlation heatmap among stocks
- 🔮 ARIMA-based forecasting with 95% confidence intervals
- 📅 Date range and stock selection filters

---

## 📂 Dataset

Historical daily stock data (2018–Present) for major NSE-listed companies obtained from Yahoo Finance.

### Companies Analyzed

- Reliance Industries
- TCS
- Infosys
- HDFC Bank
- ICICI Bank
- State Bank of India
- ITC
- Hindustan Unilever
- Bharti Airtel
- Larsen & Toubro

---

## ⚙️ Methodology

1. Compute daily percentage returns.
2. Calculate 20-day rolling mean and volatility.
3. Detect anomalies using Z-scores.
4. Identify abnormal price movements.
5. Perform statistical tests on return distributions.
6. Analyze correlations among different stocks.
7. Forecast future stock prices using ARIMA models.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- SciPy
- Statsmodels

---

## 📁 Project Structure

```
Stock_Market_Anomaly_Detector
│
├── app.py                     # Streamlit dashboard
├── preprocessing.py           # Data preprocessing pipeline
├── stock_data.csv             # Raw stock data
├── processed_stock_data.csv   # Processed dataset
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Stock_Market_Anomaly_Detector.git
cd Stock_Market_Anomaly_Detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Statistical Analysis

The dashboard incorporates several statistical tools:

- **ADF Test** for checking stationarity of return series.
- **Jarque-Bera Test** for testing normality.
- **Shapiro-Wilk Test** for distribution analysis.
- **Correlation Matrix** to understand relationships among stocks.
- **ARIMA(1,1,1)** model for short-term forecasting.

---

## 📷 Dashboard Components

- Sidebar controls
- Stock price chart with anomaly markers
- Key metrics dashboard
- Rolling volatility plot
- Return distribution histogram
- Statistical test results
- Correlation heatmap
- ARIMA forecast with confidence intervals

---

## 🎯 Applications

- Financial anomaly detection
- Exploratory market analysis
- Volatility monitoring
- Statistical analysis of stock returns
- Time-series forecasting
- Educational and research purposes

---

## 👨‍💻 Author

Developed as part of the **MTH208 Data Analytics Project** using Python and Streamlit.
