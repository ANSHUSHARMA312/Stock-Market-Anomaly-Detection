import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

## new imports
from scipy.stats import shapiro
from statsmodels.tsa.stattools import adfuller
from statsmodels.stats.stattools import jarque_bera
## end new imports

## another new import
from statsmodels.tsa.arima.model import ARIMA
## end another new import


st.title("📈 Stock Market Anomaly Detection")

df = pd.read_csv(
    "processed_stock_data.csv",
    parse_dates=["Date"]
)

# Sidebar
st.sidebar.header("Controls")

ticker = st.sidebar.selectbox(
    "Select Company",
    sorted(df["Ticker"].unique())
)

# Filter data
stock = df[df["Ticker"] == ticker]

start_date = st.sidebar.date_input(
    "Start Date",
    stock["Date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    stock["Date"].max()
)

stock = stock[
    (stock["Date"] >= pd.to_datetime(start_date)) &
    (stock["Date"] <= pd.to_datetime(end_date))
]


# st.subheader(ticker)
st.subheader(f"{ticker} Stock Price")

# making dashbord more professional
col1, col2, col3 = st.columns(3)

with col1:
    total_anomalies = stock["Anomaly"].sum()
    st.metric(
        "Total Anomalies",
        int(total_anomalies)
    )

with col2:
    st.metric(
        "Average Return (%)",
        round(stock["Return"].mean(), 2)
    )

with col3:
    st.metric(
        "Maximum Volatility",
        round(stock["RollingSD"].max(), 2)
    )

fig = go.Figure()

# Price line
fig.add_trace(
    go.Scatter(
        x=stock["Date"],
        y=stock["Close"],
        mode="lines",
        name="Close Price"
    )
)

# Price anomalies
anom = stock[stock["Anomaly"]]

fig.add_trace(
    go.Scatter(
        x=anom["Date"],
        y=anom["Close"],
        mode="markers",
        marker=dict(color="red", size=7),
        name="Price Anomaly"
    )
)

st.plotly_chart(fig, use_container_width=True)


# anomaly table
st.subheader("Detected Anomalies")

anomaly_table = stock[
    stock["Anomaly"]
][[
    "Date",
    "Close",
    "Return",
    "Z_Score"
]]

st.dataframe(
    anomaly_table,
    use_container_width=True
)
# end anomaly table


## step 9
st.subheader("20-Day Rolling Volatility")

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=stock["Date"],
        y=stock["RollingSD"],
        mode="lines",
        name="Volatility"
    )
)

st.plotly_chart(fig2, use_container_width=True)


# step 10

st.subheader("Return Distribution")

fig3 = px.histogram(
    stock,
    x="Return",
    nbins=50
)

st.plotly_chart(fig3, use_container_width=True)

# == end step 10 ==


## step 11 ===
st.header("Statistical Tests")

returns = stock["Return"].dropna()

if len(returns) > 20:

    adf_p = adfuller(returns)[1]

    jb_p = jarque_bera(returns)[1]

    sample = returns.sample(
        min(5000, len(returns))
    )

    sw_p = shapiro(sample)[1]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ADF p-value",
            f"{adf_p:.6f}"
        )

    with col2:
        st.metric(
            "Jarque-Bera p-value",
            f"{jb_p:.6f}"
        )

    with col3:
        st.metric(
            "Shapiro-Wilk p-value",
            f"{sw_p:.6f}"
        )

# end step 11 ===


## step 12 ==
pivot = df.pivot(
    index="Date",
    columns="Ticker",
    values="Return"
)

corr = pivot.corr().round(2)

# end step 12 ==


# step 13 ==
st.header("Correlation Heatmap")

fig4 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Viridis"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# end step 13 ==


# step 14 ==
st.header("ARIMA Forecast")

close_series = stock["Close"].dropna()

if len(close_series) > 100:

    model = ARIMA(
        close_series,
        order=(1, 1, 1)
    )

    fit = model.fit()

    # some changes
    forecast_result = fit.get_forecast(
        steps=30
    )

    forecast = forecast_result.predicted_mean

    conf_int = forecast_result.conf_int()

    # changes ends here

    future_dates = pd.date_range(
        stock["Date"].max(),
        periods=31
    )[1:]

    fig5 = go.Figure()

    fig5.add_trace(
        go.Scatter(
            x=stock["Date"],
            y=stock["Close"],
            name="Historical"
        )
    )

    fig5.add_trace(
        go.Scatter(
            x=future_dates,
            y=forecast,
            name="Forecast"
        )
    )

    fig5.add_trace(
        go.Scatter(
            x=future_dates,
            y=conf_int.iloc[:, 0],
            mode="lines",
            line=dict(width=0),
            showlegend=False
        )
    )

    fig5.add_trace(
        go.Scatter(
            x=future_dates,
            y=conf_int.iloc[:, 1],
            mode="lines",
            fill="tonexty",
            fillcolor="rgba(0,100,80,0.2)",
            line=dict(width=0),
            name="95% CI"
        )
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

# end step 14 ==


# final section
st.header("About")

st.write("""
This project detects unusual stock market behaviour using
Z-score based anomaly detection and volume spike analysis.

It performs:

• Statistical testing using ADF, Jarque-Bera and Shapiro-Wilk tests.

• Correlation analysis among major NSE stocks.

• ARIMA-based forecasting with confidence intervals.

Dataset:
Yahoo Finance (2018-Present)

Companies analysed:
Reliance, TCS, Infosys, HDFC Bank, ICICI Bank,
SBIN, ITC, Hindustan Unilever, Bharti Airtel and L&T.
""")

# end final section