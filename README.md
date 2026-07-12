# Indian Data-Analyst Job-Market Intelligence Dashboard

## Problem
Indian data-analyst hiring is booming, but there's no clear, current picture of which specific skills are actually in demand, where, and at what level. This project answers: if you want a Data Analyst job in India right now, what should you learn, and where should you apply?

## Data source & collection method
1,160 live job postings pulled directly from the Adzuna API (api.adzuna.com) across 6 Indian cities (Bengaluru, Mumbai, Delhi, Hyderabad, Pune, Chennai), collected via a Python script hitting Adzuna's official job-search endpoint — not scraped, not a pre-existing dataset.

## Approach
- Python (requests, pandas) to pull and clean postings
- SQLite + SQL for aggregation (postings by city, salary by city, salary disclosure rate)
- Keyword-based skill-tag extraction across job descriptions

## Key findings
- **Top 5 in-demand skills**: SQL (136 postings, 11.7%), Excel (119, 10.3%), RAG (95, 8.2%), ETL (94, 8.1%), Python (78, 6.7%)
- **GenAI/RAG has already gone mainstream**: RAG outranks Python and Power BI in mention frequency — a clear signal that Retrieval-Augmented Generation is now an expected skill, not a niche differentiator, in Indian data-analyst hiring
- **Hiring volume is more distributed than expected**: Bengaluru (250), Hyderabad (249), and Pune (242) are within a few postings of each other — Bengaluru is not the runaway leader the "hire in Bangalore" conventional wisdom suggests. Mumbai (209) and Chennai (158) follow; Delhi trails significantly (52)
- **Salary transparency is low**: only 18.2% of postings (211 of 1,160) disclose any salary range at all, making compensation benchmarking genuinely difficult for candidates
- **Where disclosed, Mumbai and Chennai pay highest on average** (~₹9.8L-16.7L and ₹8.6L-18.7L respectively for min/max bands), while Delhi's disclosed range is lowest (~₹7.2L-12.3L)

## Business recommendation
For someone entering the Data Analyst job market in India today: prioritize SQL and Excel first (still the two most-requested fundamentals), then build working familiarity with RAG/GenAI tools — it now appears more often than core Python skills and is a genuine differentiator most candidates aren't yet demonstrating. Don't over-index applications on Bengaluru alone; Hyderabad and Pune carry nearly identical hiring volume and likely less applicant competition.

## Tools
Python, SQL (SQLite), Power BI, Adzuna API

## Dashboard
https://munna54-8.github.io/indian-data-analyst-job-market-dashboard/dashboard/job_market_dashboard.html
