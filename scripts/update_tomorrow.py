import json
from datetime import date, timedelta

with open("calendar.json") as f:
    calendar = json.load(f)

tomorrow = (date.today() + timedelta(days=1)).isoformat()
value = calendar.get(tomorrow, "❓")

with open("tomorrow.json", "w") as f:
    json.dump({"value": value}, f)
