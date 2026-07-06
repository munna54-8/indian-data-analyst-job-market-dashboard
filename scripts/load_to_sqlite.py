import sqlite3
import pandas as pd

df = pd.read_csv("data/clean/jobs_clean.csv")

conn = sqlite3.connect("data/clean/jobs.db")
df.to_sql("jobs", conn, if_exists="replace", index=False)
conn.close()

print(f"Loaded {len(df)} rows into data/clean/jobs.db (table: jobs)")