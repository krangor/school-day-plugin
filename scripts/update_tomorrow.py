import json
from datetime import datetime, timedelta
import pytz

# Use Eastern Time (ET) — includes automatic handling of daylight saving time
eastern = pytz.timezone("America/Toronto")
now = datetime.now(eastern)
tomorrow = (now + timedelta(days=1)).date().isoformat()

# Load the calendar
with open("calendar.json") as f:
    calendar = json.load(f)

# Look up the value
value = calendar.get(tomorrow, "❓")

# Save to tomorrow.json
with open("tomorrow.json", "w") as f:
    json.dump({"value": value}, f)
