class Appointment:
    def __init__(self, appointmentId=None, patientId=None, doctorId=None, appointmentDate=None,
                 description=None):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description

    def print_details(self):
        print(f"Appointment ID: {self.appointmentId}")
        print(f"Patient ID: {self.patientId}")
        print(f"Doctor ID: {self.doctorId}")
        print(f"Appointment Date: {self.appointmentDate}")
        print(f"Description: {self.description}")