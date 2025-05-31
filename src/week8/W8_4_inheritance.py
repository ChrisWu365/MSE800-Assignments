'''
Activity W8-4: single inheritance in python
 
Write a Python program using single inheritance.
Create two classes: Animal (parent class) and Dog (child class).
Add a simple method in each class to demonstrate how single inheritance works.
After writing the code, briefly explain how it works.
Finally, share your code and explanation here.
'''
class Animal:
    def print_a(self):
        print("This is Animal class!")

class Dog(Animal):
    def print_d(self):
        print("This is Dog class!")

dog = Dog()
dog.print_a() # invoke method inherited from parent class(Animal)
dog.print_d() # invoke method in Dog class