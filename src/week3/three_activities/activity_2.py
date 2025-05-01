"""
Activity 2: Simple Student Grading System Using classes
Task: Create students, record their grades, and show results.
"""
# pip install tabulate
# from tabulate import tabulate
from dataclasses import dataclass

@dataclass
class Student:
    """Class for keeping track of a student."""
    student_no: str
    name: str

@dataclass
class Course:
    """Class for keeping track of a course."""
    course_no: str
    name: str

@dataclass
class StudentCourseGrade:
    """Class for keeping track of the grade of a course for a student"""
    student_no: str
    course_no: str
    grade: str

students = []
courses = []
student_course_grades = []

# create students
student_number_input = int(input('How many students do you want to create: '))
for i in range(student_number_input):
    student_no, student_name = input('Enter the student number and name(separated by one whitespace): ').split()
    students.append(Student(student_no, student_name))

# print(tabulate(students, headers=['Student No.', 'Name']))
student_table_headers = ('Student No.', 'Name')
print('\t'.join(student_table_headers))
for obj in students:
    print(f'\t{obj.student_no}\t{obj.name}')

# create courses
course_number_input = int(input('How many courses do you want to create: '))
for i in range(course_number_input):
    course_no, name = input('Enter the course number and name(separated by one whitespace): ').split()
    courses.append(Course(course_no, name))

# print(tabulate(courses, headers=['Course No.', 'Name']))
course_table_headers = ('Course No.', 'Name')
print('\t'.join(course_table_headers))
for obj in courses:
    print(f'\t{obj.course_no}\t{obj.name}')

# input grades for each course according to the input 
print('Please enter course grades for each student in the order of the course list(separated by one whitespace)!')
student_course_grade_arr = []
for student_obj in students:
    student_course_grades_input = input(f'Enter course grades for student [ {student_obj.student_no} - {student_obj.name} ]: ').split()
    student_course_grade_record = []
    student_course_grade_record.extend([student_obj.student_no, student_obj.name])
    
    for i, course in enumerate(courses):
        grade = student_course_grades_input[i]
        student_course_grades.append(StudentCourseGrade(student_obj.student_no, course.course_no, grade))
        student_course_grade_record.append(grade)

    student_course_grade_arr.append(student_course_grade_record)

# print student course grade results
result_table_headers = []
result_table_headers.extend(['Student No.', 'Student Name'])
for obj in courses:
    result_table_headers.append(obj.name)

print('\t'.join(result_table_headers))

for record in student_course_grade_arr:
    print('\t'.join(record))