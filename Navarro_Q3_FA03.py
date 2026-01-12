Students = [1, 2, 3, 4, 5]

Subjects = ["Math", "Science", "History"]

Scores = [
      [85, 99, 75, 76, 87], 
      [95, 80, 68, 56, 78], 
      [88, 77, 68, 84, 93]
      ]

for s in range(len(Students)):
    print("Student", Students[s])
    for sub in range(len(Subjects)):
        print(" ", Subjects[sub], ":", Scores[sub][s])
    print()

#totals
for i in range(len(Subjects)):
    total = sum(Scores[i])
    print(Subjects[i], "Total:", total)
    print()
print()

#averages
for i in range(len(Subjects)):
    total = sum(Scores[i])
    average = total / len(Students)
    print(Subjects[i], "Average:", average)
print()

print("Highest score (overall):", max(map(max, Scores)))
print("Lowest score (overall):", min(map(min, Scores)))

print()
