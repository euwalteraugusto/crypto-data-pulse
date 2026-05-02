import requests

def fetch_bitcoin_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

    params = {
        "vs_currency": "usd",
        "days": 365
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Erro na API: {response.status_code}")

    return response.json()