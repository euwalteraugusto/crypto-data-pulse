def generate_insights(df):
    max_price = df["price"].max()
    min_price = df["price"].min()

    best_day = df.loc[df["price"].idxmax(), "date"]
    worst_day = df.loc[df["price"].idxmin(), "date"]

    return {
        "max_price": max_price,
        "min_price": min_price,
        "best_day": best_day,
        "worst_day": worst_day
    }