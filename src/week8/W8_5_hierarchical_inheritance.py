'''
Activity W8-5: Hierarchical inheritance in python
 
To extend Activity W8-4, add another class named 'Cat' as a child class with a simple method to demonstrate hierarchical inheritance. Share your result with a short description here.
'''
class Animal:
    def make_a_noise_base(self):
        print("This is Animal class!")

    def make_a_noise(self):
        print("This is make_a_noise method in Animal class!")

class Dog(Animal):
    def make_a_noise(self):
        print("This is Dog class!")

class Cat(Animal):
    def make_a_noise(self):
        print("This is Cat class!")

dog = Dog()
dog.make_a_noise_base() # invoke method inherited from parent class(Animal)
dog.make_a_noise() # invoke method in Dog class

# class Cat and Dog both inherited from the same parent class(Animal)
cat = Cat()
cat.make_a_noise_base() # invoke method inherited from parent class(Animal)
cat.make_a_noise() # invoke method in Cat class