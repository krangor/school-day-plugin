import json
from datetime import date

with open("calendar.json", encoding="utf-8") as f:
    calendar = json.load(f)

today = date.today().isoformat()
value = calendar.get(today, "❓")

with open("today.json", "w", encoding="utf-8") as f:
    json.dump({"value": value}, f, indent=2, ensure_ascii=False)
