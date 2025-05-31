'''
Activity W8-6: Demonstrate the best use of inheritance for the following task
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am a person. My name is {self.name}, and I am {self.age} years old!")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I am a Student. My name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}!")

student = Student("Chris", 100, 123456)
 # invoke introduce() method in the Student class which has overwritten the method in the parent class
student.introduce()