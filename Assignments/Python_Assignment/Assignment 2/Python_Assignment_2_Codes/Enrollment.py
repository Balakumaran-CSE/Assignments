from Student import Student
from Course import Course
class Enrollment(Student, Course):
    def __init__(self, Enrollment_ID=None, Student_ID=None, Course_ID=None, Enrollment_Date=None):
        Student.__init__(self, Student_ID)
        Course.__init__(self, Course_ID)
        self.Enrollment_ID = Enrollment_ID
        self.Enrollment_Date = Enrollment_Date

    def GetStudent(self):
        return self.Student_ID

    def GetCourse(self):
        return self.Course_ID