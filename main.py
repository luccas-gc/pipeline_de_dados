import pandas as pd
import src.pipeline as pipeline
import sqlite3

def main():
    df = pd.read_csv("data/sales.csv")
    conn = sqlite3.connect("data/processed/sales.db")

    pipeline.run_pipeline(pipeline.prepare_data(df), conn)

    conn.close()

if __name__ == "__main__":
    main()