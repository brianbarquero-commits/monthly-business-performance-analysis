import pandas as pd

df = pd.read_csv("monthly_time_data.csv")

df["date"] = pd.to_datetime(df["date"])

df["month"] = df["date"].dt.to_period("M")

df["profit"] = df["revenue"] - df["cost"]

df["margin"] = df["profit"] / df["revenue"]

monthly = (
    df.groupby("month", as_index=False)
    .agg(
        total_revenue=("revenue", "sum"),
        total_profit=("profit", "sum"),
    )
)

monthly["weighted_margin"] = (
    monthly["total_profit"] / monthly["total_revenue"]
)

monthly = monthly.sort_values("month")

monthly["profit_ma_3"] = (
    monthly["total_profit"].rolling(window=3).mean()
)

monthly["revenue_ma_3"] = (
    monthly["total_revenue"].rolling(window=3).mean()
)

forecast_avg = monthly["total_profit"].tail(3).mean()

forecast_avg_df = pd.DataFrame({
    "month": ["next_month_forecast"],
    "method": ["3_month_average"],
    "estimated_profit": [forecast_avg]
})


monthly["profit_change"] = monthly["total_profit"].diff()

avg_change = monthly["profit_change"].tail(3).mean()

forecast_trend = monthly["total_profit"].iloc[-1] + avg_change

forecast_trend_df = pd.DataFrame({
    "month": ["next_month_forecast"],
    "method": ["trend_projection"], 
    "estimated_profit": [forecast_trend]
})

forecast_df = pd.concat([forecast_avg_df, forecast_trend_df])

forecast_df.to_csv("forecast_report.csv", index=False)

print("Forecast Report")
print(forecast_df)