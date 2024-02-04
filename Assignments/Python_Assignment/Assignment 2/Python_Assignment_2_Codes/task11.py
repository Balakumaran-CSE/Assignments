import mysql.connector

def generate_enrollment_report(conn, course_name):
    try:
        cursor = conn.cursor(dictionary=True )

        cursor.execute("SELECT students.student_id, students.first_name, students.last_name, students.email "
                       "FROM students "
                       "JOIN enrollments ON students.student_id = enrollments.student_id "
                       "JOIN courses ON enrollments.course_id = courses.course_id "
                       "WHERE courses.course_name = %s", (course_name,))

        enrollment_records = cursor.fetchall()

        print(f"Enrollment Report for Course: {course_name}")
        print("--------------------------------------------------")
        print("Student ID | First Name | Last Name | Email")
        print("--------------------------------------------------")
        for record in enrollment_records:
            print(f"{record['student_id']} | {record['first_name']} | {record['last_name']} | {record['email']}")
            report_content=''

        for record in enrollment_records:
            report_content += f"{record['student_id']} | {record['first_name']} | {record['last_name']} | {record['email']}\n"

            with open('records', 'w') as file:
                file.write(report_content)

    except Exception as e:
        print(f"Error during report generation: {e}")

def retrieve_enrollment(con,course_id):
    cur=con.cursor(dictionary=True)
    cur.execute("SELECT * FROM Enrollments WHERE course_id=%s",(course_id,))
    res=cur.fetchall()
    print(f"\nRetrieving enrollment records for the specified course {course_id}")
    print("--------------------------------------------------")
    print("Enroll ID | Stud ID | Course ID| Enrollment Date")
    print("--------------------------------------------------")
    for i in res:
        print(f"{i['enrollment_id']} | {i['student_id']} | {i['course_id']} | {i['enrollment_date']}")

try:
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', database='sisdb', port='3306')
    course_name_to_report = "Computer Science"
    generate_enrollment_report(conn, course_name_to_report)
    retrieve_enrollment(conn,101)
except Exception as e:
    print(f"Error: {e}")
