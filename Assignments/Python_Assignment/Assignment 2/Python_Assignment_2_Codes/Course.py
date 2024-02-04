
class Course:

    def __init__(self,Course_ID=None,Course_Name=None,Course_Code=None,Instructor_Name=None):
        self.Course_ID=Course_ID
        self.Course_Name = Course_Name
        self.Course_Code = Course_Code
        self.Instructor_Name = Instructor_Name
        self.course_assigned = []
        self.enrolled_students = []
        self.enrollments = []
    def AssignTeacher(self, teacher):
        if teacher not in self.course_assigned:
            self.course_assigned.append(teacher)
            print(f"{teacher.First_Name} has been assigned to the course {self.Course_Name}")
        else:
            print(f"{teacher.First_Name} has already been assigned to this course")

    def AssignStudent(self, student):
        if student not in self.course_assigned:
            enrollment = Enrollment(student=student, course=self)
            self.enrollments.append(enrollment)
            self.enrolled_students.append(student)
            print(f"{student.First_Name} has been enrolled to the course {self.Course_Name}")
        else:
            print(f"{student.First_Name} has already been enrolled to this course")

    def UpdateCourseInfo(self,Course_Name,Course_Code,Instructor_Name):
        self.Course_Name = Course_Name
        self.Course_Code = Course_Code
        self.Instructor_Name = Instructor_Name

    def DisplayCourseInfo(self):
        print('-' * 50)
        print("Course Detail: ")
        print("Course Id: ",self.Course_ID)
        print("Course Name: ", self.Course_Name)
        print("Course Code: ", self.Course_Code)
        print("Instructor Name: ", self.Instructor_Name)

    def GetEnrollments(self,student):
        print("Enrolled Students")
        for student in self.enrolled_students:
            print(f"Student {student.First_Name} has enrolled in {self.Course_Code} course")
    def GetTeacher(self,teacher):
        print("Assigned Teacher")
        for teacher in self.course_assigned:
            print(f"Teacher {teacher.First_Name} has assigned to {self.Course_Code} course")