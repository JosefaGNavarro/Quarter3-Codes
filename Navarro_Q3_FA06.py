student = {}

student['name'] = input("What's your name? ")
student['age'] = input("What's your age? ")
student['subject'] = input("What's your favorite subject? ")

for key, value in student.items():
    print(f"{key.capitalize()}: {value}")