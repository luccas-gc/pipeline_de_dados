import pandas as pd

# cria coluna "Total" e formata datas com "pd.datetime" para manuseio
def prepare_data(df):
    df_copy = df.copy()
    df_copy["total"] = df_copy["price"] * df_copy["quantity"]
    df_copy["date"] = pd.to_datetime(df_copy["date"])
    return df_copy

def load_db(df, conn):
    df.to_sql("all_sales", conn, if_exists="replace", index=True)
    print("Tabela all_sales criada")
    return df

def faturamento_total(df, conn):
    faturamento_total = df.groupby("product")["total"].sum().sort_values(ascending=False)
    faturamento_total.to_sql("sales_by_product_revenue", conn, if_exists="replace", index=True)
    print("Tabela sales_by_product_revenue criada")
    return faturamento_total

def faturamento_dia(df, conn):
    faturamento_por_dia = df.groupby("date")["total"].sum().sort_values(ascending=False)
    faturamento_por_dia.to_sql("sales_by_day", conn, if_exists="replace", index=True)
    print("Tabela sales_by_day criada")
    return faturamento_por_dia

def faturamente_semana(df, conn):
    iso_calendar = df["date"].dt.isocalendar()
    df["ano_semana"] = iso_calendar["year"].astype(str) + "-W" + iso_calendar["week"].astype(str).str.zfill(2)
    faturamente_por_semana = df.groupby("ano_semana")["total"].sum().sort_values(ascending=False)
    faturamente_por_semana.to_sql("sales_by_week", conn, if_exists="replace", index=True)
    print("Tabela saleb_by_week criada")
    return faturamente_por_semana

def faturamento_mes(df, conn):
    df["month"] = df["date"].dt.to_period("M").astype(str)
    faturamento_por_mes = df.groupby("month")["total"].sum().sort_values(ascending=False)
    faturamento_por_mes.to_sql("saleb_by_month", conn, if_exists="replace", index=True)
    print("Tabela saleb_by_month criada")
    return faturamento_por_mes

def mais_vendidos(df, conn):
    produtos = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
    produtos.to_sql("sales_by_product_quantity", conn, if_exists="replace", index=True)
    print("Tabela sales_by_product_quantity criada")
    return produtos

def run_pipeline(df, conn):
    load_db(df, conn)
    faturamento_total(df, conn)
    mais_vendidos(df, conn)
    faturamento_dia(df, conn)
    faturamente_semana(df, conn)
    faturamento_mes(df, conn)
    print("Pipeline Executada")