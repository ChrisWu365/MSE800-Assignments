from database import create_connection
import sqlite3

def add_user_course(user_id, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO user_course (user_id, course_id) VALUES (?, ?)", (user_id, course_id))
        conn.commit()
        print(" Course added to user successfully.")
    except sqlite3.IntegrityError:
        print(" User ID and Course ID must be correct.")
    conn.close()

def view_courses_by_user_name(user_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT u.id User_ID, u.name User_Name, c.name Course_Name FROM user_course uc, users u, course c where uc.user_id = u.id and uc.course_id = c.id and u.name = ?", (user_name, ))
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_users_by_course_id(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT c.id Course_ID, c.name Course_Name, u.name User_Name FROM user_course uc, users u, course c where uc.user_id = u.id and uc.course_id = c.id and c.id = ?", (course_id, ))
    rows = cursor.fetchall()
    conn.close()
    return rows
