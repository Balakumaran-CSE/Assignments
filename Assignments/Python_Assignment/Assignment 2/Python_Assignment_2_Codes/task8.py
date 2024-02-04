import mysql.connector
from datetime import datetime, date
def add_student(conn,id, first_name, last_name, birth_date, email, phone):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students  VALUES (%s, %s, %s, %s, %s, %s)",
            (id,first_name, last_name, birth_date, email, phone))
        print("Data inserted successfully...")
        conn.commit()
    except Exception as e:
        print(f"Error during student enrollment: {e}")
        conn.rollback()
def enrol_student(conn, student_id, courses):
    try:
        cursor = conn.cursor()
        for course in courses:
            # Enroll the student in each specified course
            cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)",
                           (student_id, course))
        print(f"Student enrolled in courses successfully.")
        conn.commit()
    except Exception as e:
        print(f"Error during course enrollment: {e}")
        conn.rollback()
try:
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', database='sisdb', port='3306')
    id=20
    first_name = 'John'
    last_name = 'Doe'
    birth_date = date(1995, 8, 15)
    email = 'john.doe@example.com'
    phone = '123-456-7890'
    add_student(conn,id, first_name, last_name, birth_date, email, phone)
    course_id=[101,112]
    enrol_student(conn,id,course_id)
except Exception as e:
    print(f"Error: {e}")

