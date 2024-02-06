class Doctor:
    def __init__(self, doctorId=None, firstName=None, lastName=None, specialization=None,
                 contactNumber=None):
        self.doctorId = doctorId
        self.firstName = firstName
        self.lastName = lastName
        self.specialization = specialization
        self.contactNumber = contactNumber

    def print_details(self):
        print(f"Doctor ID: {self.doctorId}")
        print(f"First Name: {self.firstName}")
        print(f"Last Name: {self.lastName}")
        print(f"Specialization: {self.specialization}")
        print(f"Contact Number: {self.contactNumber}")