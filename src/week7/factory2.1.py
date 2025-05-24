from abc import ABC, abstractmethod
 
class Factory(ABC):
   
    @abstractmethod
    def create_product(self, kind=None):
        pass
 
class AnimalFactory(Factory):
    def __init__(self):
        pass
 
    def create_product(self, kind=None):
        if kind == "dog":
            animal = Dog()
        elif kind == "cat":
            animal = Cat()
 
        return animal
 
class DogFactory(Factory):
   
    def create_product(self, kind=None):
        return Dog()
 
class CatFactory(Factory):
   
    def create_product(self, kind=None):
        return Cat()
 
class Animals(ABC):
 
    @abstractmethod
    def run(self):
        pass
 
class Dog(Animals):
 
    def run(self):
        print(f"I'm a Dog, I can run!!")
 
 
class Cat(Animals):
    def __init__(self):
        pass
 
    def run(self):
        print(f"I'm a Cat, I can run!!")
 
 
 
 
 
# client
# create Dog instance directly
dog = Dog()
dog.run()

# there is nothing in create_product method of DogFactory, so we should use AnimalFactory which creates animal based on kind input parameter
factory = AnimalFactory()
# create Dog instance with AnimalFactory, assign "dog" kind as input
dog = factory.create_product("dog") 
dog.run()

# create Dog instance with DogFactory
dogFactory = DogFactory()
dog = dogFactory.create_product()
dog.run()