import sqlite3
import pandas as pd

conn = sqlite3.connect("data/clean/jobs.db")


df = pd.read_sql_query("SELECT id, skills_found FROM job_skills", conn)
df["skills_found"] = df["skills_found"].apply(eval)  # stored as string repr of a list
exploded = df.explode("skills_found").dropna()
exploded.columns = ["job_id", "skill"]
exploded.to_csv("data/clean/skills_long.csv", index=False)


jobs = pd.read_sql_query("SELECT location, salary_min, salary_max, category, company FROM jobs", conn)
jobs.to_csv("data/clean/jobs_for_dashboard.csv", index=False)

conn.close()
print(f"Exported {len(exploded)} skill mentions and {len(jobs)} job rows for the dashboard")