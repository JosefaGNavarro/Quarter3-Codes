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

print()
print("UPDATING SCORES...\n")
print()
# Update
Scores[0][3] = 79
Scores[1][4] = 63

for s in range(len(Students)):
    print("Student", Students[s])
    for sub in range(len(Subjects)):
        print(" ", Subjects[sub], ":", Scores[sub][s])
    print()