names = ["Zoe", "Frio", "Joseph"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# total steps per day
daily = []

for day in range(len(days)): #day aka column
    day_total = 0
    for per in range(len(names)): #person aka row
        day_total += steps[per][day]
    daily.append(day_total) #auto adds all total to daily
    print((days[day]), "total steps:", (day_total)) #auto picks the day from the list and prints the total
print()
  

# most active day
max_steps_day = max(daily)
max_day_index = daily.index(max_steps_day)

print("Most active day overall:", (days[max_day_index]), "with", (max_steps_day), "steps")
print()
