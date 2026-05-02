import pandas as pd

def transform_data(data):
    prices = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    volumes = pd.DataFrame(data["total_volumes"], columns=["timestamp", "volume"])
    market_caps = pd.DataFrame(data["market_caps"], columns=["timestamp", "market_cap"])

    df = prices.merge(volumes, on="timestamp").merge(market_caps, on="timestamp")

    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.drop("timestamp", axis=1, inplace=True)

    return df