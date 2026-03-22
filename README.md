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

---

## Estrutura do projeto
├─ data/
│ └─ sales.csv # Dados de entrada
├─ data/processed/ # Banco de dados SQLite gerado
│ └─ sales.db # Database gerado após executar o projeto
├─ src/
│ └─ pipeline.py # Funções para processar dados
├─ main.py # Script principal que executa o pipeline
├─ requirements.txt # Dependências do projeto
└─ README.md

## ▶️ Como executar

1. Clone o repositório
- git clone <https://github.com/luccas-gc/pipeline_de_dados>
- cd <pipeline_de_dados>

2. Crie e ative um ambiente virtual
- python -m venv venv
- venv\Scripts\activate

3. Instale as Dependências
- pip install requirements.txt

4. Execute main.py
- python main.py

## 📁 Saída

O banco será criado em:
- data/processed/sales.db