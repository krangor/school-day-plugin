import requests
import json

headers = {
    "x-api-key": "live_TdM5IGyU91dlffzlWUgF7mst1azY7tdJ9chLr4iqdIUDzdnlZouDYSB38ziPMFrN"
}

response = requests.get("https://api.thecatapi.com/v1/images/search", headers=headers)
data = response.json()

cat_url = data[0]["url"]

payload = {
    "url": cat_url,
    "title": "Random Cat",
    "explanation": "Here's your hourly cat!"
}

with open("cat.json", "w") as f:
    json.dump(payload, f, indent=2)
