# 📊 Pipeline de Dados

Prática de **Pandas** e **SQLite**, simulando uma pipeline de dados (ETL).

---

## 🧠 Objetivo

Treinar conceitos básicos de:

- Manipulação de dados com Pandas  
- Agrupamentos e análises  
- Uso de SQLite  
- Estrutura de pipeline  

---

## 🚀 O que o projeto faz

- Lê um arquivo CSV com dados de vendas
- Cria a coluna `total` com o total faturado
- Cria as tabelas:
  - **all_sales** (Todos os dados formatados)
  - **sales_by_month** (Faturamento por Mês)
  - **sales_by_week** (Faturamento por Semana)
  - **sales_by_day** (Faturamento por Dia)
  - **sales_by_product_quantity** (Produtos mais vendidos)
  - **sales_by_product_revenue** (Produtos mais lucrativo)
- Salva tudo em um banco de dados SQLite

## Como executar

Basta clonar o repositório com:
- git clone <URL do repositório>

Ativar o ambiente virtual e instalar as depencências
- python -m venv venv
- venv\Scripts\activate
- pip install requirements.txt

Executar main.py
- python main.py

## 📁 Saída

O banco será criado em:
- data/processed/sales.db