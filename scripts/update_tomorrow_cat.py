import requests
import json
from datetime import datetime, timedelta

# Compute tomorrow's date
tomorrow_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

# Load tomorrow's day value
with open("calendar.json") as f:
    calendar_data = json.load(f)
    day_value = calendar_data.get(tomorrow_date, "❓")

# Fetch a random cat image using your API key
headers = {
    "x-api-key": "live_TdM5IGyU91dlffzlWUgF7mst1azY7tdJ9chLr4iqdIUDzdnlZouDYSB38ziPMFrN"
}
response = requests.get("https://api.thecatapi.com/v1/images/search", headers=headers)
data = response.json()
cat_url = data[0]["url"]

# Compose explanation
explanation = (
    f"Meow! Tomorrow is Day {day_value}!"
    if day_value not in ["❓", "🛌", "📚", "🏕️"]
    else "Meow! No school tomorrow!"
)

# Write to tomorrow_cat.json
payload = {
    "url": cat_url,
    "explanation": explanation
}

with open("tomorrow_cat.json", "w") as f:
    json.dump(payload, f, indent=2)

print(f"✅ Saved tomorrow's cat and message to tomorrow_cat.json ({tomorrow_date})")
