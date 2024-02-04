from Student import Student
from Course import Course
from Teacher import Teacher
from Payment import Payment
from SIS import SIS
def main():
    sis = SIS()

    student4 = Student(Student_ID="TN001", First_Name="Arvind", Last_Name="Kumar", DOB="1993-05-12",
                       Email="arvind.kumar@example.com", Phone_NO="9876543210")
    student5 = Student(Student_ID="TN002", First_Name="Kavya", Last_Name="Raj", DOB="1990-08-25",
                       Email="kavya.raj@example.com", Phone_NO="8765432109")

    course5 = Course(Course_ID="TN101", Course_Name="Tamil Literature", Course_Code="TAML101",
                     Instructor_Name="Ramachandran")
    course6 = Course(Course_ID="TN102", Course_Name="History", Course_Code="HISTTN101",
                     Instructor_Name="Prof. Senthil Kumar")

    teacher5 = Teacher(Teacher_ID="TN01", First_Name="Dr.Sanjay", Last_Name="Ramachandran", Email="dr.ram@gmail.com")
    teacher6 = Teacher(Teacher_ID="TN02", First_Name="Prof.Senthil ", Last_Name="Kumar",
                       Email="prof.senthil@gmail.com")

    payment4 = Payment(Payment_ID="TNP001", Student_ID="TN001", Amount=800, Payment_Date="2024-02-05")
    payment5 = Payment(Payment_ID="TNP002", Student_ID="TN002", Amount=700, Payment_Date="2024-02-08")
    course5.enrolled_students.append(student5)
    sis.students.append(student4)
    sis.students.append(student5)
    sis.teachers.append(teacher5)
    sis.teachers.append(teacher6)
    student4.enrolled_courses.append(course5)
    teacher5.assigned_courses.append(course5)
    teacher5.assigned_courses.append(course6)

    print("Assigning teachers to courses: ")
    sis.AssignTeacherToCourse(teacher5, course5)
    sis.AssignTeacherToCourse(teacher6, course6)
    print("\nGetting Enrollment Details for students: ")
    sis.GetEnrollmentsForStudent(student4)
    print("\nGetting the courses assigned to a particular teacher: ")
    sis.GetCoursesForTeacher(teacher5)
    print("\nMaking payments: ")
    sis.RecordPayment(student5, 500, "2024-02-01")
    sis.RecordPayment(student4, 600, "2024-02-02")

    print("\nCalculated course statistics: ")
    sis.CalculateCourseStatistics(course5)
    sis.AddEnrollment(student5, course6)
    print("\nAssigning courses to a particular teacher")
    sis.AssignCourseToTeacher(course5, teacher6)
    print("\nGenerating Payment report for students:")
    sis.GeneratePaymentReport(student4)
    print("\nGenerating Enrollment report for Courses:")
    sis.GenerateEnrollmentReport(course5)
if __name__ == "__main__":
    main()
