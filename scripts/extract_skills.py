import sqlite3
import pandas as pd

SKILLS = [
    "sql", "excel", "power bi", "tableau", "python", "r programming",
    "looker", "statistics", "a/b testing", "machine learning",
    "google sheets", "vba", "data visualization", "etl",
    "google analytics", "spss", "sas", "big query", "snowflake",
    "aws", "azure", "gcp", "airflow", "spark", "hadoop",
    "llm", "rag", "genai", "chatgpt", "prompt engineering", "nlp"
]

def extract(description):
    if not isinstance(description, str):
        return []
    desc_lower = description.lower()
    return [skill for skill in SKILLS if skill in desc_lower]

conn = sqlite3.connect("data/clean/jobs.db")
df = pd.read_sql_query("SELECT id, description FROM jobs", conn)

df["skills_found"] = df["description"].apply(extract)

skill_counts = {}
for skills in df["skills_found"]:
    for skill in skills:
        skill_counts[skill] = skill_counts.get(skill, 0) + 1

skill_df = pd.DataFrame(
    sorted(skill_counts.items(), key=lambda x: x[1], reverse=True),
    columns=["skill", "postings_mentioning"]
)
skill_df.to_csv("data/clean/skill_frequency.csv", index=False)

df[["id", "skills_found"]].to_sql("job_skills", conn, if_exists="replace", index=False)
conn.close()

print(skill_df.to_string(index=False))
print("\nSaved to data/clean/skill_frequency.csv")