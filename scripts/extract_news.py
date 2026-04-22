import requests
import json

API_KEY = "YOUR_KEY"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

with open("/opt/airflow/scripts/news.json", "w") as f:
    json.dump(data, f)

print("News extracted successfully")