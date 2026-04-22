import json
import pandas as pd

with open("/opt/airflow/scripts/news.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

for article in data.get("articles", []):
    rows.append({
        "source": article.get("source", {}).get("name"),
        "title": article.get("title"),
        "author": article.get("author")
    })

df = pd.DataFrame(rows)

df.to_csv("/opt/airflow/scripts/news.csv", index=False)

print("CSV created successfully")