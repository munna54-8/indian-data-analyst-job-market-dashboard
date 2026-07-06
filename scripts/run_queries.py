import sqlite3
import pandas as pd

conn = sqlite3.connect("data/clean/jobs.db")

with open("sql/analysis.sql", "r") as f:
    sql_script = f.read()

queries = [q.strip() for q in sql_script.split(";") if q.strip()]

for i, query in enumerate(queries, 1):
    print(f"\n--- Query {i} ---")
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))

conn.close()