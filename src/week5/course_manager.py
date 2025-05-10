from database import create_connection
import sqlite3

def add_course(name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (name, unit) VALUES (?, ?)", (name, unit))
        conn.commit()
        print(" Course added successfully.")
    except sqlite3.IntegrityError:
        print(" Course name must be unique.")
    conn.close()

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_course(name_or_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course WHERE name LIKE ? or id LIKE ?", ('%' + name_or_id + '%', '%' + name_or_id + '%'))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_course(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM course WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()
    print("🗑️ Course deleted.")

def update_course_name(course_id, course_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE course SET NAME = ? WHERE ID = ?", (course_name, course_id))
    conn.commit()
    conn.close()
    print(f"{cursor.rowcount} course name updated.")
