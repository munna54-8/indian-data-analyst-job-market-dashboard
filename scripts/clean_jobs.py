import json
import glob
import pandas as pd

def load_all_raw():
    records = []
    for filepath in glob.glob("data/raw/*.json"):
        with open(filepath, "r", encoding="utf-8") as f:
            postings = json.load(f)
        for job in postings:
            records.append({
                "id": job.get("id"),
                "title": job.get("title"),
                "company": job.get("company", {}).get("display_name"),
                "location": job.get("location", {}).get("display_name"),
                "category": job.get("category", {}).get("label"),
                "salary_min": job.get("salary_min"),
                "salary_max": job.get("salary_max"),
                "created": job.get("created"),
                "description": job.get("description"),
                "redirect_url": job.get("redirect_url"),
            })
    return pd.DataFrame(records)

def main():
    df = load_all_raw()
    print(f"Total postings loaded (with duplicates): {len(df)}")

    df = df.drop_duplicates(subset="id")
    print(f"After removing duplicates: {len(df)}")

    df = df.dropna(subset=["title", "description"])
    print(f"After dropping rows missing title/description: {len(df)}")

    df.to_csv("data/clean/jobs_clean.csv", index=False)
    print("Saved to data/clean/jobs_clean.csv")

if __name__ == "__main__":
    main()