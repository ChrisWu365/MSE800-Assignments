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
'''
Function design:
1. get_users() to get user information for verifying a user when login
2. get_cars_from_repository() to get all car information from repository (e.g., database)
3. get_cars_by_availability() to display all available cars
4. get_current_timestamp() to get current timestamp to print time in log file
5. write_file() to write log file
'''
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

 