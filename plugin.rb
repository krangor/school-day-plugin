plugin :face_day do
  polling_url "https://cdn.jsdelivr.net/gh/krangor/school-day-plugin/calendar.json"

  screen do
    today = Date.today.strftime("%Y-%m-%d")
    {
      day_display: data[today] || "❓"
    }
  end
end
