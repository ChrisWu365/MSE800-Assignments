'''
Activity 5-2: Add one more option to the code
 
Update the sample code in activity 5-1 to this activity: 
Add one more option (No.6) to do the advanced search based on ID and name

Activity W5-3 : continue the coding using the your sample code
 
Add one more Table "course" (name, ID and unit columns ) with two functionality insert and search based on course_ID and user name
'''
from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, update_user_name
from course_manager import add_course, view_courses, search_course, delete_course, update_course_name
from user_course_manager import add_user_course, view_courses_by_user_name, view_users_by_course_id

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Update User name by ID")

def menu_course():
    print("\n==== Course Manager ====")
    print("1. Add Course")
    print("2. View All Courses")
    print("3. Search Course by Name or ID")
    print("4. Exit")

def menu_user_course():
    print("\n==== User Course Manager ====")
    print("1. Add a user to a course")
    print("2. Search All courses selected by user name")
    print("3. Search All Users who have selected the course by course ID")
    print("4. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        elif choice == '6':
            user_id, user_name = input("Enter user ID and name to update the user's name: ").split()
            user_id = int(user_id)
            update_user_name(user_id, user_name)
        else:
            print("Invalid choice, try again.")

    while True:
        menu_course()
        choice = input("Select an option (1-4): ")
        if choice == '1':
            name = input("Enter name: ")
            unit = input("Enter unit: ")
            add_course(name, unit)
        elif choice == '2':
            courses = view_courses()
            for course in courses:
                print(course)
        elif choice == '3':
            name_or_id = input("Enter name or id to search: ")
            courses = search_course(name_or_id)
            for course in courses:
                print(course)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

    while True:
        menu_user_course()
        choice = input("Select an option (1-4): ")
        if choice == '1':
            user_id = input("Enter user id: ")
            course_id = input("Enter course id: ")
            add_user_course(user_id, course_id)
        elif choice == '2':
            user_name = input("Enter user name to search selected courses: ")
            courses = view_courses_by_user_name(user_name)
            for course in courses:
                print(course)
        elif choice == '3':
            course_id = input("Enter course ID to search attended users: ")
            users = view_users_by_course_id(course_id)
            for user in users:
                print(user)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
