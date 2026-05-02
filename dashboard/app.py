import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from analysis.insights import generate_insights
from dotenv import load_dotenv

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Crypto Data Pulse",
    page_icon="📊",
    layout="wide"
)

# =========================
# CONEXÃO COM BANCO
# =========================

load_dotenv()

engine = create_engine(
    f"postgresql://postgres:{os.getenv('DB_PASSWORD')}@localhost:5433/crypto"
)

# =========================
# CARREGAMENTO DE DADOS (CORRIGIDO)
# =========================
@st.cache_data
def load_data():
    query = """
        SELECT *
        FROM bitcoin_market
        ORDER BY date
    """
    df = pd.read_sql(query, engine)
    df["date"] = pd.to_datetime(df["date"])
    return df


with st.spinner("Carregando dados..."):
    df = load_data()

# =========================
# TÍTULO
# =========================
st.title("📊 Crypto Data Pulse")
st.caption("Análise de preço, volume e volatilidade do Bitcoin")

# =========================
# SIDEBAR (FILTROS) — CORRIGIDO ORDEM
# =========================
st.sidebar.header("Filtros")

min_date = df["date"].min()
max_date = df["date"].max()

date_range = st.sidebar.date_input(
    "Período",
    [min_date, max_date]
)

if len(date_range) == 2:
    df = df[
        (df["date"] >= pd.to_datetime(date_range[0])) &
        (df["date"] <= pd.to_datetime(date_range[1]))
    ]

# =========================
# VALIDAÇÃO MÍNIMA (EVITA QUEBRA)
# =========================
if df.empty:
    st.warning("Nenhum dado encontrado para o período selecionado.")
    st.stop()

# =========================
# KPIs (ROBUSTO)
# =========================
if len(df) > 1:
    last_price = df["price"].iloc[-1]
    first_price = df["price"].iloc[0]
else:
    last_price = first_price = df["price"].iloc[0]

variation = ((last_price - first_price) / first_price) * 100

# proteção caso coluna não exista
volatility = df["daily_return"].std() if "daily_return" in df.columns else 0

col1, col2, col3 = st.columns(3)

col1.metric("Preço Atual (USD)", f"${last_price:,.2f}")
col2.metric("Variação no Período", f"{variation:.2f}%")
col3.metric("Volatilidade", f"{volatility:.4f}")

# =========================
# GRÁFICO PRINCIPAL
# =========================
st.subheader("📈 Evolução do Preço")

fig_price = px.line(
    df,
    x="date",
    y="price",
    title="Preço do Bitcoin ao longo do tempo"
)

st.plotly_chart(fig_price, use_container_width=True)

# =========================
# MÉDIA MÓVEL
# =========================
st.subheader("📉 Tendência (Média Móvel 7 dias)")

if "rolling_mean_7" in df.columns:
    fig_ma = px.line(
        df,
        x="date",
        y="rolling_mean_7",
        title="Média móvel de 7 dias"
    )
    st.plotly_chart(fig_ma, use_container_width=True)
else:
    st.info("Média móvel não disponível nos dados.")

# =========================
# VOLATILIDADE
# =========================
st.subheader("📊 Volatilidade")

if "volatility_7" in df.columns:
    fig_vol = px.line(
        df,
        x="date",
        y="volatility_7",
        title="Volatilidade (7 dias)"
    )
    st.plotly_chart(fig_vol, use_container_width=True)
else:
    st.info("Volatilidade não disponível nos dados.")

# =========================
# INSIGHTS
# =========================
insights = generate_insights(df)

st.subheader("📌 Insights automáticos")

st.write(f"Maior preço: ${insights['max_price']:,.2f}")
st.write(f"Menor preço: ${insights['min_price']:,.2f}")
st.write(f"Melhor dia: {insights['best_day']}")
st.write(f"Pior dia: {insights['worst_day']}")

# =========================
# DADOS BRUTOS
# =========================
with st.expander("📄 Ver dados brutos"):
    st.dataframe(df.tail(50))