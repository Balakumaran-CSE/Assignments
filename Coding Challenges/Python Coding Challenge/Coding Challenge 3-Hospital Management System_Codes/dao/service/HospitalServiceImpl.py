from dao.service.IHospitalService import IHospitalService
import mysql.connector

from myexceptions.exception import PatientNumberNotFoundException


class HospitalServiceImpl(IHospitalService):
    def __init__(self, database_con):
        self.database_con = database_con

    def generate_appointment_id(self):
        connection = self.database_con

        cur = connection.cursor()
        cur.execute("SELECT MAX(AppointmentID) FROM Appointment")
        appointment_id = cur.fetchone()[0]
        if appointment_id is None:
            appointment_id = 1
        else:
            appointment_id += 1
        return appointment_id

    def get_appointment_by_id(self, appointment_id):
        connection = self.database_con
        appointment_data = None
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM Appointment WHERE appointmentId = %s", (appointment_id,))
                appointment_data = cursor.fetchone()

            except mysql.connector.Error as err:
                print(f"Error: {err}")
            return appointment_data

    def get_appointments_for_patient(self, patient_id):
        connection = self.database_con
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM Appointment WHERE patientID = %s", (patient_id,))
                appointment_data = cursor.fetchone()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                raise

            if not appointment_data:
                raise PatientNumberNotFoundException(f"Patient with ID {patient_id} not found.")

            return appointment_data

    def get_appointments_for_doctor(self, doctor_id):
        connection = self.database_con
        appointment_data = None
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM Appointment WHERE doctorID = %s", (doctor_id,))
                appointment_data = cursor.fetchone()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            return appointment_data

    def schedule_appointment(self, appointment_data):
        connection = self.database_con
        appointment_id = self.generate_appointment_id()

        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Appointment VALUES (%s,%s,%s,%s,%s)",
                           (appointment_id, appointment_data['patientId'], appointment_data['doctorId'],
                            appointment_data['appointmentDate'], appointment_data['description'],))
            connection.commit()
            print("Appointment scheduled successfully!")
        except Exception as e:
            print(f"Error scheduling appointment: {e}")

    def update_appointment(self, appointment):
        appointment_id=appointment.get('appointmentId')
        patientId = appointment.get('patientId')
        doctorId = appointment.get('doctorId')
        appointmentDate = appointment.get('appointmentDate')
        description = appointment.get('description')

        connection=self.database_con
        try:
            cursor=connection.cursor()
            cursor.execute('''  
                        UPDATE Appointment
                        SET patientId = %s,
                            doctorId = %s,
                            appointmentDate = %s,
                            description = %s  
                        WHERE appointmentID = %s
                        ''',
                           (patientId,doctorId,appointmentDate,description,appointment_id))
            connection.commit()
        except Exception as e:
            print(e)


    def cancel_appointment(self, appointment_id):
        connection=self.database_con
        try:
            cursor=connection.cursor()
            cursor.execute("DELETE FROM Appointment WHERE appointmentID = %s",(appointment_id,))
            connection.commit()
        except Exception as e:
            print(e)