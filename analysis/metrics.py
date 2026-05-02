def add_metrics(df):
    df = df.sort_values("date")

    df["daily_return"] = df["price"].pct_change()

    df["rolling_mean_7"] = df["price"].rolling(7).mean()

    df["volatility_7"] = df["daily_return"].rolling(7).std()

    return df