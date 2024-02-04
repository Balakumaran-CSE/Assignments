import mysql.connector


def get_course(con, course_id):
    cur = con.cursor()
    cur.execute("SELECT * FROM Courses WHERE course_id=%s", (course_id,))
    res = cur.fetchone()  # Use fetchone to retrieve a single row
    print("Retrieving the course record from the database based on the course code")
    print(res)


def add_teacher(con, teacher_id, first_name, last_name, email):
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO Teacher VALUES (%s, %s, %s, %s)", (teacher_id, first_name, last_name, email))
        print("Data inserted successfully...")
        con.commit()
    except Exception as e:
        print(e)


def assign_teacher(con, teacher_id, course_id):
    cur2 = con.cursor()
    cur2.execute("UPDATE Courses SET teacher_id=%s WHERE course_id=%s", (teacher_id, course_id))
    print(f"Teacher {teacher_id} has been assigned to the Course {course_id}")
    con.commit()


try:
    con = mysql.connector.connect(host='localhost', user='root', passwd='root', database='sisdb', port='3306')

    get_course(con, course_id=302)

    add_teacher(con, teacher_id=19,
                first_name='Sarah',
                last_name='Smith',
                email='sarah.smith@example.com')

    assign_teacher(con, teacher_id=19, course_id=302)

except Exception as e:
    print(e)

