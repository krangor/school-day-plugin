import json
from datetime import datetime, timedelta
import pytz

# Load the calendar
with open("calendar.json") as f:
    calendar = json.load(f)

# Get Eastern Time now
eastern = pytz.timezone("America/Toronto")  # or "America/New_York"
now_et = datetime.now(eastern)

# Get tomorrow's date in ISO format
tomorrow = (now_et + timedelta(days=1)).date().isoformat()

# Look up tomorrow’s value in the calendar
value = calendar.get(tomorrow, "❓")

# Write the result to tomorrow.json
with open("tomorrow.json", "w") as f:
    json.dump({"value": value}, f)
