
class Student:
    def __init__(self,Student_ID=None,First_Name=None,Last_Name=None,DOB=None,Email=None,Phone_NO=None):
        self.Student_ID=Student_ID
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.DOB = DOB
        self.Email = Email
        self.Phone_NO = Phone_NO
        self.enrolled_courses=[]
        self.payment_made=[]
        self.enrollments = []
    def EnrollInCourse(self,course):
        if course not in self.enrolled_courses:
            enrollment = Enrollment(student=self, course=course)
            self.enrollments.append(enrollment)
            print(f"Student {self.Student_ID} enrolled in course {course.Course_ID}")
        else:
            print(f"Student {self.Student_ID} is already enrolled in course {course.Course_ID}")

    def UpdateStudentInfo(self,First_Name,Last_Name,DOB,Email,Phone_NO):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.DOB = DOB
        self.Email = Email
        self.Phone_NO = Phone_NO

    def MakePayment(self,payment):
        self.payment_made.append(payment)
        print(f"Payment of {payment.Amount} made by {self.First_Name} on {payment.Payment_Date}")

    def DisplayStudentInfo(self):
        print('-' * 50)
        print("Students Detail: ")
        print(f"Student ID: {self.Student_ID}")
        print(f"Name: {self.First_Name} {self.Last_Name}")
        print(f"Date of Birth: {self.DOB}")
        print(f"Email: {self.Email}")
        print(f"Phone Number: {self.Phone_NO}")

    def GetEnrolledCourses(self):
        print('-' * 50)
        print(f"Enrolled Courses for {self.Student_ID}:")
        for course in self.enrolled_courses:
            print(f"{course.Course_ID}-{course.Course_Name}")

    def GetPaymentHistory(self):
        print(f"Payment History for {self.Student_ID}: ")
        for payment in self.payment_made:
            print(f"Payement Amount: {payment.Amount}, Date: {payment.Payment_Date} ")
