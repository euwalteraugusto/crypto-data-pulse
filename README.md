# 📊 Crypto Data Pulse — Pipeline de Dados e Dashboard Analítico

## 📌 Visão Geral

O **Crypto Data Pulse** é um projeto de engenharia de dados ponta a ponta que simula um fluxo real de mercado financeiro, desde a ingestão de dados públicos até a visualização analítica em dashboard interativo.

O objetivo principal foi construir uma solução prática que integra:

- Coleta de dados de mercado em tempo real via API pública
- Processamento e transformação de dados com Python
- Persistência em banco de dados PostgreSQL
- Cálculo de métricas financeiras
- Visualização interativa com Streamlit

---

## 🧠 Problema Resolvido

Em cenários reais de análise de ativos financeiros, dados costumam estar dispersos, sem estrutura e sem camada analítica pronta.

Este projeto resolve esse problema ao:

- Centralizar dados em banco relacional
- Automatizar processamento de métricas
- Permitir exploração visual de séries temporais
- Reduzir dependência de análises manuais em planilhas

---

## 🏗️ Arquitetura do Projeto

```

crypt-data-pulse/
│
├── analysis/
│   ├── insights.py        # Geração de insights analíticos
│   └── metrics.py         # Cálculo de métricas financeiras
│
├── dashboard/
│   └── app.py             # Interface Streamlit
│
├── database/
│   └── connection.py      # Conexão com PostgreSQL
│
├── etl/
│   ├── extract.py         # Coleta de dados
│   ├── transform.py       # Processamento
│   └── load.py            # Persistência
│
├── main.py                # Orquestração do pipeline
├── .env                   # Variáveis de ambiente
└── README.md

```

---

## 🔄 Fluxo de Dados

1. **Extração**
   - Dados de mercado são coletados via API pública de criptomoedas

2. **Transformação**
   - Normalização de dados
   - Cálculo de métricas como:
     - retorno diário
     - média móvel
     - volatilidade

3. **Carga (Load)**
   - Persistência dos dados em PostgreSQL

4. **Visualização**
   - Dashboard interativo em Streamlit com:
     - evolução de preço
     - tendência
     - volatilidade
     - insights automáticos

---

## 📊 Dashboard

O dashboard fornece uma visão analítica dos dados com:

- Série temporal de preços
- Média móvel de tendência
- Indicadores de volatilidade
- KPIs financeiros
- Insights automáticos gerados pelo sistema

---

## 🧪 Tecnologias Utilizadas

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Streamlit
- Plotly
- dotenv
- APIs públicas de dados financeiros

---

## 📌 Principais Features

- Pipeline de dados completo (ETL)
- Persistência em banco relacional
- Análise de séries temporais
- Dashboard interativo
- Cálculo de métricas financeiras
- Sistema modular e extensível

---

## 📈 Insights Gerados

O sistema gera automaticamente:

- Maior preço no período
- Menor preço no período
- Melhor e pior dia do ativo
- Tendências de curto prazo

---

## 🚀 Possíveis Evoluções

- Orquestração com Airflow
- Containerização com Docker
- Suporte a múltiplos ativos (BTC, ETH, etc.)
- Deploy em nuvem (AWS/GCP)
- Alertas automáticos de mercado
- KPIs financeiros avançados (Sharpe Ratio, Drawdown)

---

## 👨‍💻 Autor

**Walter Fonseca**

- LinkedIn: [walteraugusto](https://www.linkedin.com/in/walteraugusto)

---

## 📎 Objetivo do Projeto

Este projeto foi desenvolvido com foco em aprendizado prático de engenharia de dados, simulação de pipeline real e construção de portfólio técnico para área de dados e software.

---
```
