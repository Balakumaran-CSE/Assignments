class Patient:
    def __init__(self, patientId=None, firstName=None, lastName=None, dateOfBirth=None,
                 gender=None, contactNumber=None, address=None):
        self.patientId = patientId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.contactNumber = contactNumber
        self.address = address

    def print_details(self):
        print(f"Patient ID: {self.patientId}")
        print(f"First Name: {self.firstName}")
        print(f"Last Name: {self.lastName}")
        print(f"Date of Birth: {self.dateOfBirth}")
        print(f"Gender: {self.gender}")
        print(f"Contact Number: {self.contactNumber}")
        print(f"Address: {self.address}")