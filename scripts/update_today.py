import json
from datetime import datetime
import pytz

# Use Eastern Time (ET) — will auto-adjust for DST
eastern = pytz.timezone("America/Toronto")
now = datetime.now(eastern)
today = now.date().isoformat()

# Load the calendar
with open("calendar.json") as f:
    calendar = json.load(f)

# Look up the value
value = calendar.get(today, "❓")

# Save to today.json
with open("today.json", "w") as f:
    json.dump({"value": value}, f)

print(f"Current Eastern time: {now}")
print(f"Using date: {today}")
print(f"Value written: {value}")
