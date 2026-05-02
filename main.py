from data_ingestion.coingecko_api import fetch_bitcoin_data
from etl.transform import transform_data
from database.connection import get_engine, save_to_db
from analysis.metrics import add_metrics
from utils.logger import get_logger

logger = get_logger(__name__)

logger.info("Coletando dados...")
logger.info("Transformando dados...")
logger.info("Salvando no banco...")

def main():
    print("Coletando dados...")
    raw_data = fetch_bitcoin_data()

    print("Transformando dados...")
    df = transform_data(raw_data)

    print("Calculando métricas...")
    df = add_metrics(df)

    print("Conectando banco...")
    engine = get_engine()

    print("Salvando no banco...")
    save_to_db(df, engine)

    print("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    main()