# Student Scores to Grades
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}

for name in student_scores:
    score = student_scores[name]
    if score > 90:
        student_grades[name] = "Outstanding"
    elif score > 80:
        student_grades[name] = "Exceeds Expectations"
    elif score > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)