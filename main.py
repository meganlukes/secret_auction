#grading
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for thing in student_scores:
  grade = ""
  if student_scores[thing] > 89:
    grade = "Fantastic"
  elif student_scores[thing] > 79:
    grade = "Very Good"
  elif student_scores[thing] > 69:
    grade = "Acceptable"
  else:
    grade = "Fail"
  student_grades[thing] = grade
print(student_grades)