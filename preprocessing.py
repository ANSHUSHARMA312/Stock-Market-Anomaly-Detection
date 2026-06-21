import os
import numpy as np
import pandas as pd

# Load raw data
df = pd.read_csv("stock_data.csv")

# Rename columns
df.rename(columns={
    "symbol": "Ticker",
    "date": "Date",
    "open": "Open",
    "high": "High",
    "low": "Low",
    "close": "Close",
    "volume": "Volume",
    "adjusted": "Adjusted"
}, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values(["Ticker", "Date"])

# Returns
df["Return"] = (
    df.groupby("Ticker")["Adjusted"]
    .pct_change()*100
)

# Rolling statistics
df["RollingMean"] = (
    df.groupby("Ticker")["Return"]
    .transform(lambda x: x.rolling(20).mean())
)

df["RollingSD"] = (
    df.groupby("Ticker")["Return"]
    .transform(lambda x: x.rolling(20).std())
)

# Z-score
df["Z_Score"] = (
    (df["Return"]-df["RollingMean"])
    / df["RollingSD"].replace(0, np.nan)
)

# Price anomaly
df["Anomaly"] = abs(df["Z_Score"]) > 3

# Volume average
df["Vol_Avg"] = (
    df.groupby("Ticker")["Volume"]
    .transform(lambda x: x.rolling(20).mean())
)

# Volume anomaly
df["Anomaly_Volume"] = (
    df["Volume"] > 2.5*df["Vol_Avg"]
)

df.to_csv("processed_stock_data.csv", index=False)

print("Preprocessing complete")


