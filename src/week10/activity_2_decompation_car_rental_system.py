'''
Function design:
1. print_menu() to print the main menu options
2. view_available_cars() to view all available cars
3. rent_car() to rent a car
4. return_car() to return a rented car
5. get_users() to get all user information for verifying a user when login
6. get_cars() to get all car information from repository (e.g., database)
7. get_current_timestamp() to print current timestamp in the log file
8. write_file() to write a log file
'''
'''
Activity Week10-2: Do decompaction for the following function With Top down for car rental System
Decompose the following function and share your results via a GitHub link. 
See the function below:
 
import datetime
 
def car_rental_system():

    cars = {

        "CAR001": {"type": "SUV", "available": True},

        "CAR002": {"type": "Sedan", "available": True},

        "CAR003": {"type": "Hatchback", "available": True}

    }

    users = ["user1", "user2"]

    rentals = {}
 
    while True:

        print("\n--- Car Rental System ---")

        print("1. View Available Cars")

        print("2. Rent a Car")

        print("3. Return a Car")

        print("4. Exit")

        choice = input("Enter your choice: ")
 
        if choice == "1":

            print("\nAvailable Cars:")

            for car_id, details in cars.items():

                if details["available"]:

                    print(f"{car_id} - {details['type']}")

            log_message = f"{datetime.datetime.now()} - Viewed available cars"

            with open("rental_log.txt", "a") as log_file:

                log_file.write(log_message + "\n")
 
        elif choice == "2":

            user_id = input("Enter your user ID: ")

            if user_id not in users:

                print("Invalid user.")

                continue
 
            print("\nAvailable Cars:")

            for car_id, details in cars.items():

                if details["available"]:

                    print(f"{car_id} - {details['type']}")

            car_id = input("Enter Car ID to rent: ")
 
            if car_id in cars and cars[car_id]["available"]:

                cars[car_id]["available"] = False

                rentals[user_id] = car_id

                print(f"{user_id} rented {car_id}")

                log_message = f"{datetime.datetime.now()} - {user_id} rented {car_id}"

                with open("rental_log.txt", "a") as log_file:

                    log_file.write(log_message + "\n")

            else:

                print("Car not available or invalid ID.")

                log_message = f"{datetime.datetime.now()} - {user_id} failed to rent {car_id}"

                with open("rental_log.txt", "a") as log_file:

                    log_file.write(log_message + "\n")
 
        elif choice == "3":

            user_id = input("Enter your user ID: ")

            if user_id in rentals:

                car_id = rentals[user_id]

                cars[car_id]["available"] = True

                del rentals[user_id]

                print(f"{user_id} returned {car_id}")

                log_message = f"{datetime.datetime.now()} - {user_id} returned {car_id}"

                with open("rental_log.txt", "a") as log_file:

                    log_file.write(log_message + "\n")

            else:

                print("No rental record found.")

                log_message = f"{datetime.datetime.now()} - {user_id} attempted return with no rental"

                with open("rental_log.txt", "a") as log_file:

                    log_file.write(log_message + "\n")
 
        elif choice == "4":

            print("Exiting system.")

            break
 
        else:

            print("Invalid choice.")

            log_message = f"{datetime.datetime.now()} - Invalid menu choice"

            with open("rental_log.txt", "a") as log_file:

                log_file.write(log_message + "\n")

 
'''
import datetime

LOG_FILE_NAME = "rental_log.txt"

def print_menu():
    """Print the main menu options"""
    print("\n--- Car Rental System ---")

    print("1. View Available Cars")

    print("2. Rent a Car")

    print("3. Return a Car")

    print("4. Exit")

def get_users():
    """Get all user information"""
    users = ["user1", "user2"]
    return users

def get_cars():
    """Get all car information from repository"""
    cars = {

        "CAR001": {"type": "SUV", "available": True},

        "CAR002": {"type": "Sedan", "available": True},

        "CAR003": {"type": "Hatchback", "available": True}

    }
    return cars

def get_current_timestamp():
    """Get the current timestamp"""
    return datetime.datetime.now()

def write_file(message, file_name=LOG_FILE_NAME):
    """Write a message to the file, default is rental_log.txt"""
    with open(file_name, "a") as file:
        file.write(message + "\n")

def view_available_cars(cars):
    """View all available cars"""
    print("\nAvailable Cars:")

    for car_id, details in cars.items():

        if details["available"]:

            print(f"{car_id} - {details['type']}")

    log_message = f"{get_current_timestamp()} - Viewed available cars"

    write_file(log_message)

def rent_car(cars, users, rentals):
    """Rent a car for a user"""
    user_id = input("Enter your user ID: ")

    if user_id not in users:

        print("Invalid user.")
        return False

    print("\nAvailable Cars:")

    for car_id, details in cars.items():

        if details["available"]:

            print(f"{car_id} - {details['type']}")

    car_id = input("Enter Car ID to rent: ")

    if car_id in cars and cars[car_id]["available"]:

        cars[car_id]["available"] = False

        rentals[user_id] = car_id

        print(f"{user_id} rented {car_id}")

        log_message = f"{get_current_timestamp()} - {user_id} rented {car_id}"

        write_file(log_message)

    else:

        print("Car not available or invalid ID.")

        log_message = f"{get_current_timestamp()} - {user_id} failed to rent {car_id}"

        write_file(log_message)
    return True

def return_car(cars, rentals):
    user_id = input("Enter your user ID: ")

    if user_id in rentals:

        car_id = rentals[user_id]

        cars[car_id]["available"] = True

        del rentals[user_id]

        print(f"{user_id} returned {car_id}")

        log_message = f"{get_current_timestamp()} - {user_id} returned {car_id}"

        write_file(log_message)

    else:

        print("No rental record found.")

        log_message = f"{get_current_timestamp()} - {user_id} attempted return with no rental"

        write_file(log_message)

def car_rental_system():

    cars = get_cars()
    users = get_users()
    rentals = {}
 
    while True:

        print_menu()

        choice = input("Enter your choice: ")
 
        if choice == "1":
            view_available_cars(cars)
        elif choice == "2":
            if not rent_car(cars, users, rentals):
                continue
        elif choice == "3":
            return_car(cars, rentals)
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")

            log_message = f"{get_current_timestamp()} - Invalid menu choice"

            write_file(log_message)

if __name__ == "__main__":
    car_rental_system()