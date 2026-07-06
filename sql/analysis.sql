-- Top 20 hiring companies
SELECT company, COUNT(*) AS postings
FROM jobs
GROUP BY company
ORDER BY postings DESC
LIMIT 20;

-- Postings by city
SELECT location, COUNT(*) AS postings
FROM jobs
GROUP BY location
ORDER BY postings DESC;

-- Postings by category
SELECT category, COUNT(*) AS postings
FROM jobs
GROUP BY category
ORDER BY postings DESC;

-- Average disclosed salary by city (where salary data exists)
SELECT location,
       ROUND(AVG(salary_min), 0) AS avg_salary_min,
       ROUND(AVG(salary_max), 0) AS avg_salary_max,
       COUNT(*) AS postings_with_salary
FROM jobs
WHERE salary_min IS NOT NULL
GROUP BY location
ORDER BY postings_with_salary DESC;

-- What share of postings actually disclose salary?
SELECT
    SUM(CASE WHEN salary_min IS NOT NULL THEN 1 ELSE 0 END) AS with_salary,
    COUNT(*) AS total,
    ROUND(100.0 * SUM(CASE WHEN salary_min IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct_disclosed
FROM jobs;