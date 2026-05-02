import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.dialects.postgresql import insert

load_dotenv()

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    return create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{db}"
    )
    
def save_to_db(df, engine):
    table = "bitcoin_market"

    for _, row in df.iterrows():
        query = insert(table).values(
            date=row["date"],
            price=row["price"],
            volume=row["volume"],
            market_cap=row["market_cap"]
        ).on_conflict_do_update(
            index_elements=["date"],
            set_={
                "price": row["price"],
                "volume": row["volume"],
                "market_cap": row["market_cap"]
            }
        )