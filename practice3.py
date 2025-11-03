#تابع محاسبه معدل
def calculate_student_gpa(student):
    grades = student["grades"] 
  gpa = sum(grades) / len(grades)
    return gpa


students = [
    {"name": "Ali", "student_id": "1", "grades": [16.75, 20, 16, 20]},
    {"name": "mohammad", "student_id": "2", "grades": [10, 15.25, 16.5, 13]},
    {"name": "zahra", "student_id": "3", "grades": [9.75, 11.5, 8.75, 10]}
]

# محاسبه و چاپ معدل هر دانشجو با استفاده از حلقه
for student in students:
    gpa = calculate_student_gpa(student)
    print(f"Student: {student['name']} (ID: {student['student_id']}) → GPA: {gpa:.2f}")
