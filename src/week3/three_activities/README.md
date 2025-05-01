# Class activities
This repository contains solutions to three class-based activities. Classes can be used to encapsulate related data and functions, which makes the code modular and easier to manage.

## Activity 1: Library Book Manager Using classes( activity_1.py )
### Classes
#### 1. Book Class
Represents a single book in the library with:
- Attributes: isbn, title

#### 2. LibraryBookManager Class
Manages the collection of books with:
- Attributes: library_name, books
- Methods:
    - add_book(self, isbn, title): Adds a new book to the books collection
    - add_books(self, books): Adds a collection of book to the books collection
    - show_books(self, page_size, page_number, search_key_word): Search books with pagination. Searching books by a key word may be a popular function that will be implemented in the future.

### How to run
Run the program using Python: 
```
python activity_1.py
```

## Activity 2: Simple Student Grading System Using classes( activity_2.py )
### Classes
#### 1. Student Class
Represents a single student with:
- Attributes: student_no, name

#### 2. Course Class
Represents a single course with:
- Attributes: course_no, name

#### 3. StudentCourseGrade Class
Represents the grade of a course for a student with:
- Attributes: student_no, course_no, grade

### How to run
Run the program using Python: 
```
python activity_2.py
```