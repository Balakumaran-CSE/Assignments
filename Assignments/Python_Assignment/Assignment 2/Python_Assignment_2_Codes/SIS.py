from Student import Student
from Course import Course
from Enrollment import Enrollment
from Teacher import Teacher
from Payment import Payment
from Exceptions import *
from datetime import datetime
class SIS:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []
        self.payments = []

    def EnrollStudentInCourse(self, student, course):
        self.students.append(student)
        self.courses.append(course)
        course.enrolled_students.append(student)
        if course not in self.courses:
            raise CourseNotFoundException(f"{course.Course_ID} not found")
        if not isinstance(student, Student):
            raise InvalidStudentDataException("Invalid student object provided")
        if student in self.students:
            raise DuplicateEnrollmentException(student.Student_ID,course.Course_ID)
        if not isinstance(course, Course):
            raise InvalidCourseDataException("Invalid course object provided")

        try:
            student.EnrollInCourse(course)
            self.students.append(student)
        except DuplicateEnrollmentException as e:
            print(f"Enrollment Error: {e}")
            raise e
        except Exception as e:
            print(f"Unexpected Error: {e}")
            raise e

    def AssignTeacherToCourse(self, teacher, course):
        self.courses.append(course)
        if teacher not in self.teachers:
            raise TeacherNotFoundException(teacher.Teacher_ID)
        if type(teacher) is not Teacher:
            raise InvalidTeacherDataException("Invalid teacher object provided")

        if type(course) is not Course:
            raise InvalidCourseDataException("Invalid course object provided")

        try:
            course.AssignTeacher(teacher)
        except TeacherNotFoundException as e:
            raise e  # Re-raise the specific exception
        except Exception as e:
            raise e  # Re-raise any unexpected exceptions

    def RecordPayment(self, student, amount, payment_date):
        if student not in self.students:
            raise StudentNotFoundException(student.Student_ID)
        if type(student) is not Student:
            raise InvalidStudentDataException("Invalid student object provided")
        if amount<0:
            raise PaymentValidationException("Invalid Amount")
        try:
            payment = Payment(Student_ID=student.Student_ID, Amount=amount, Payment_Date=payment_date)
            student.MakePayment(payment)
            self.payments.append(payment)
        except PaymentValidationException as e:
            raise e
        except Exception as e:
            raise e

    def GeneratePaymentReport(self, student):
        print(f"Payment Report for Student {student.Student_ID} - {student.First_Name} {student.Last_Name}:")
        for payment in student.payment_made:
            print(f"Payment Amount: {payment.Amount}, Date: {payment.Payment_Date}")

    def GenerateEnrollmentReport(self, course):
        print(f"Enrollment Report for Course {course.Course_Name}:")
        for student in course.enrolled_students:
            print(f"Student ID: {student.Student_ID}, Name: {student.First_Name} {student.Last_Name}")

    def CalculateCourseStatistics(self, course):
        enrolled_students_count = len(course.enrolled_students)
        total_payments = sum(payment.Amount for student in course.enrolled_students for payment in student.payment_made)
        print('-' * 50)
        print(f"Statistics for Course {course.Course_Name}:")
        print(f"Number of Enrollments: {enrolled_students_count}")
        print(f"Total Payments: {total_payments}")

    def AddEnrollment(self,student,course):
        self.students.append(student)
        student.enrollments.append(student)
        course.enrollments.append(course)

    def AssignCourseToTeacher(self,course,teacher):
        self.teachers.append(teacher)
        course.AssignTeacher(teacher)

    def AddPayment(self,payment,student):
        self.payments.append(payment)
        student.MakePayment(payment)

    def GetEnrollmentsForStudent(self, student):
        if student not in self.students:
            raise StudentNotFoundException(student.Student_ID)
        print(f"Enrollments for Student {student.First_Name} {student.Last_Name}:")

        enrolled_courses=[course for course in student.enrolled_courses]
        for course in enrolled_courses:
            print(f"{course.Course_ID}-{course.Course_Name}-{course.Course_Code}")

    def GetCoursesForTeacher(self, teacher):
        if teacher not in self.teachers:
            raise TeacherNotFoundException(teacher.Teacher_ID)

        teacher_courses = [course for course in teacher.assigned_courses]
        print('-' * 50)
        print(f"Courses assigned to Teacher {teacher.First_Name} {teacher.Last_Name}:")
        for course in teacher_courses:
            print(f"{course.Course_ID}-{course.Course_Name}")
