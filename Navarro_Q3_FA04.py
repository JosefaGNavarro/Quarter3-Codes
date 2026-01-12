names = ["Zoe", "Frio", "Joseph"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

totals = []  # to store total steps for each person

for i in range(len(names)):
    total = sum(steps[i])
    totals.append(total)
    print(names[i], "'s total steps:", total)

#highest total
maxstep = max(totals)
max_index = totals.index(maxstep)  # get index of person with max steps

print("\nPerson with highest total steps:", names[max_index], "with", maxstep, "steps")
print()

#difference
mistep = min(totals)
difference = maxstep - mistep

print("Difference between highest and lowest total:", difference, "steps")
print()