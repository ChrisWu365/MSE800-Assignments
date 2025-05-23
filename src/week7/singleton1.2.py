class RentalManager:
    _instance = None
 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RentalManager, cls).__new__(cls)
            cls._instance.cars_available = ["Toyota", "Honda", "Ford"]
        return cls._instance
 
    def rent_car(self, car_name):
        print("Address of car_name in rent_car method is: ", id(car_name))
        if car_name in self.cars_available:
            self.cars_available.remove(car_name)
            print(f"{car_name} has been rented.")
        else:
            print(f"{car_name} is not available.")
 
    def show_available_cars(self):
        print("Available cars:", self.cars_available)

    def show_cars_available_address(self):
        print("cars_available address is:", id(self.cars_available))

 
 
manager1 = RentalManager()
manager2 = RentalManager()
car_name = "Toyota"
print("Address of car_name is: ", id(car_name))
manager1.rent_car(car_name)
manager2.show_cars_available_address()  # Affects both because it's the same instance
 
print("Are both managers the same object?", manager1 is manager2)