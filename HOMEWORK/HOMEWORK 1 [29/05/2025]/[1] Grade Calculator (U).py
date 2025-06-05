mark = float(input("Enter your mark : "))

if mark >= 90:
    grade = 'A'
elif mark > 80 and mark < 90:
    grade = 'B'
elif mark >= 70 and mark < 80:
    grade = 'C'
elif mark >= 60 and mark < 70:
    grade = 'D'
else:
    grade = 'E'

print("Your grade is: ", grade)