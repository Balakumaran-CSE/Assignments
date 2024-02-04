class DuplicateEnrollmentException(Exception):
    def __init__(self, student_id, course_id):
        super().__init__(f"Student {student_id} is already enrolled in course {course_id}")

class CourseNotFoundException(Exception):
    def __init__(self, course_id):
        super().__init__(f"Course {course_id} not found")

class StudentNotFoundException(Exception):
    def __init__(self, student_id):
        super().__init__(f"Student {student_id} not found")

class TeacherNotFoundException(Exception):
    def __init__(self, teacher_id):
        super().__init__(f"Teacher {teacher_id} not found")

class PaymentValidationException(Exception):
    def __init__(self, message):
        super().__init__(f"Payment validation failed: {message}")

class InvalidStudentDataException(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid student data: {message}")

class InvalidCourseDataException(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid course data: {message}")

class InvalidEnrollmentDataException(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid enrollment data: {message}")

class InvalidTeacherDataException(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid teacher data: {message}")

class InsufficientFundsException(Exception):
    def __init__(self, student_id, course_id):
        super().__init__(f"Student {student_id} does not have enough funds to enroll in course {course_id}")