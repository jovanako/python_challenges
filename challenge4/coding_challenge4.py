wash_duration_minutes = 21
num_days_in_month = 30

def seconds_to_minutes(seconds):
  minutes = seconds // 60
  remainder_seconds = seconds % 60
  return (minutes, remainder_seconds)

def wash_hands(washes_per_day, num_months):
  total_days = num_months * num_days_in_month
  num_washes = total_days * washes_per_day
  seconds_spent_washing = num_washes * wash_duration_minutes
  minutes, seconds = seconds_to_minutes(seconds_spent_washing)
  return f"{minutes} minutes and {seconds} seconds"

print(wash_hands(8, 7))