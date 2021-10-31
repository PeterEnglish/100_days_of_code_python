student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    score = student_scores[student]
    if score>90:
        grade = 'Outstanding'
    elif score>80:
        grade = 'Acceptable'
    elif score>70:
        grade = 'Not Great'
    else:
        grade = 'Fail'
    student_grades[student]=grade

# 🚨 Don't change the code below 👇
print(student_grades)