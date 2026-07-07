import pandas as pd
import sqlite3

conn = sqlite3.connect("data/clean/jobs.db")

print("=== TOP 15 SKILLS ===")
skills = pd.read_csv("data/clean/skill_frequency.csv")
print(skills.head(15).to_string(index=False))

print("\n=== CITY POSTING COUNTS ===")
df = pd.read_sql_query("SELECT location, salary_min, salary_max FROM jobs", conn)
cities = ["Bengaluru", "Bangalore", "Mumbai", "Delhi", "Hyderabad", "Pune", "Chennai"]

def extract_city(loc):
    if not isinstance(loc, str):
        return "Unknown"
    for c in cities:
        if c.lower() in loc.lower():
            return "Bengaluru" if c == "Bangalore" else c
    return "Other"

df["city"] = df["location"].apply(extract_city)
print(df["city"].value_counts().to_string())

print("\n=== SALARY DISCLOSURE RATE ===")
total = len(df)
with_salary = df["salary_min"].notna().sum()
pct = round(100 * with_salary / total, 1)
print(f"With salary: {with_salary} / {total} = {pct}%")

conn.close()