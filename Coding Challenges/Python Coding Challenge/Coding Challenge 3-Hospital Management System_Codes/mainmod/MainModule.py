from datetime import date

from dao.service.IHospitalService import IHospitalService
from dao.service.HospitalServiceImpl import HospitalServiceImpl
from myexceptions.exception import PatientNumberNotFoundException
from util.DBConnection import DBConnection

from util.PropertyUtil import PropertyUtil

def main():

    connection_details = {
        'host': 'localhost',
        'user': 'root',
        'passwd': 'root',
        'port': '3306',
        'dbname': 'HospitalManagementSystem'
    }

    db_connection = DBConnection.get_connection(connection_details)
    hospital_service = HospitalServiceImpl(db_connection)
    print("Hospital Management System :")
    while True:
        print('''
                1 ---> Get Appointment Details By appointment ID
                2 ---> Get Appointment for Patient
                3 ---> Get Appointment for Doctor
                4 ---> Schedule Appointment
                5 ---> Update Appointment
                6 ---> Cancel Appointment
                7 ---> Exit
                
             ''')
        choice = input('Enter Your choice(1-7): ')

        try:
            if choice == '1':
                appointment_id=int(input("Enter your appointment ID: "))
                appointments=hospital_service.get_appointment_by_id(appointment_id)
                print("Appointment ID: ",appointments['appointmentId'])
                print("Patient ID: ", appointments['patientId'])
                print("Doctor ID: ", appointments['doctorId'])
                print("Appointment Date: ", appointments['appointmentDate'])
                print("Description: ", appointments['description'])

            if choice == '2':
                patient_id=input("Enter your patient ID: ")
                appointments=hospital_service.get_appointments_for_patient(patient_id)
                print("Appointment ID: ", appointments['appointmentId'])
                print("Patient ID: ", appointments['patientId'])
                print("Doctor ID: ", appointments['doctorId'])
                print("Appointment Date: ", appointments['appointmentDate'])
                print("Description: ", appointments['description'])
            if choice == '3':
                doctor_id=input("Enter your Doctor ID: ")
                appointments=hospital_service.get_appointments_for_doctor(doctor_id)
                print("Appointment ID: ", appointments['appointmentId'])
                print("Patient ID: ", appointments['patientId'])
                print("Doctor ID: ", appointments['doctorId'])
                print("Appointment Date: ", appointments['appointmentDate'])
                print("Description: ", appointments['description'])

            if choice == '4':
                new_appointment = {
                    'patientId': input("Enter patient ID: "),
                    'doctorId': input("Enter doctor ID: "),
                    'appointmentDate': date.today(),
                    'description': input("Enter Description if any: ")
                }
                hospital_service.schedule_appointment(new_appointment)
                print("Appointment confirmed")

            if choice == '5':
                new_appointment = {
                    'appointmentId': input("Enter appointment ID: "),
                    'patientId': input("Enter patient ID: "),
                    'doctorId': input("Enter doctor ID: "),
                    'appointmentDate': input("Enter the appointment date: "),
                    'description': input("Enter Description if any to change: ")
                }
                hospital_service.update_appointment(new_appointment)
                print("Appointment Updated Successfully....")

            if choice == '6':
                appointment_id=int(input("Enter your appointment ID: "))
                hospital_service.cancel_appointment(appointment_id)
                print("Your appointment has been cancelled successfully...")
            if choice == '7':
                print("Exiting....")
                break
        except PatientNumberNotFoundException as e:
            print(f"Patient Number Not Found: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()