class Teacher:
    def __init__(self,Teacher_ID=None,First_Name=None,Last_Name=None,Email=None):
        self.Teacher_ID=Teacher_ID
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Email = Email
        self.assigned_courses=[]

    def DisplayTeacherInfo(self):
        print('-' * 50)
        print("Teacher Info: ")
        print(f"Teacher ID: {self.Teacher_ID}")
        print(f"Name: {self.First_Name} {self.Last_Name}")
        print(f"Email: {self.Email}")

    def UpdateTeacherInfo(self,First_Name,Last_Name,Email):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Email = Email

    def AssignToCourse(self, course):
        if course not in self.assigned_courses:
            self.assigned_courses.append(course)
            print('-' * 50)
            print(f"Teacher {self.First_Name} assigned to course {course.Course_Name}")
        else:
            print('-' * 50)
            print(f"Teacher {self.First_Name} is already assigned to course {course.Course_Name}")

    def GetAssignedCourses(self):
        print('-' * 50)
        print(f"Courses assigned to Teacher {self.First_Name}:")
        for course in self.assigned_courses:
            print(f"{course.Course_ID}-{course.Course_Name}")