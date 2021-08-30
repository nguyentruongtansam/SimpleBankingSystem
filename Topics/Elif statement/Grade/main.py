student_score = int(input())
max_score = int(input())

percentage = student_score / max_score * 100
grades = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}

if percentage <= 100:
    for grade in grades:
        if percentage >= grades[grade]:
            print(grade)
            break
else:
    pass
