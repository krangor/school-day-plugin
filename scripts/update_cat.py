import requests
import json
from datetime import datetime

# Load today's day value
with open("today.json") as f:
    today_data = json.load(f)
    day_value = today_data.get("value", "❓")

# Fetch a random cat image
headers = {
    "x-api-key": "live_TdM5IGyU91dlffzlWUgF7mst1azY7tdJ9chLr4iqdIUDzdnlZouDYSB38ziPMFrN"
}
response = requests.get("https://api.thecatapi.com/v1/images/search", headers=headers)
data = response.json()
cat_url = data[0]["url"]

# Compose explanation
explanation = f"Meow! Today is Day {day_value}!" if day_value not in ["❓", "🛌", "📚", "🏕️"] else "Meow! No school today!"

# Write to cat.json
payload = {
    "url": cat_url,
    "explanation": explanation
}

with open("cat.json", "w") as f:
    json.dump(payload, f, indent=2)
