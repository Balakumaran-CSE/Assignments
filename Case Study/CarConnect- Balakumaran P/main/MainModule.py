from dao.service.AuthenticationService import AuthenticationService
from dao.service.CustomerService import CustomerService
from datetime import date

from dao.service.ReportGenerator import ReportGenerator
from dao.service.VehicleService import VehicleService
from dao.service.ReservationService import ReservationService
from dao.service.AdminService import AdminService
from dao.service.DatabaseContext import DatabaseContext
from exception.CustomExceptions import AuthenticationException, ReservationException, VehicleNotFoundException, \
    AdminNotFoundException, DatabaseConnectionException


def display_menu():
    print("Car Reservation System")
    print("1. Customer Section")
    print("2. Admin Section")
    print("3. Exit")


def main():
    db_context = DatabaseContext()
    try:
        db_context.connect()
    except DatabaseConnectionException as e:
        print(e)

    # Service instances
    customer_service = CustomerService(db_context)
    vehicle_service = VehicleService(db_context)
    reservation_service = ReservationService(db_context)
    admin_service = AdminService(db_context)
    authunticate_service = AuthenticationService(db_context)
    report=ReportGenerator(db_context)
    while True:
        display_menu()
        section_choice = input("Enter your choice (1-3): ")

        if section_choice == '1':
            print("Customer Section:")
            print("1. Log In\n2. Create New Account\n3. Go Back")

            customer_auth_choice = input("Enter your choice (1-3): ")

            if customer_auth_choice == '1':
                try:
                    customer_username = input("Enter your username: ")
                    customer_password = input("Enter your password: ")

                    if authunticate_service.authenticate_user(customer_username, customer_password):
                        print("Login successful!\n")

                        while True:
                            print("Customer Operations:")
                            customer_choice = input(
                                "1. View Your Details\n2. Update Your Details\n3. Remove Your Account\n"
                                "4. View Vehicle Details\n5. View Available Vehicles\n6. Reserve a Vehicle\n"
                                "7. Update Reservation \n8. Cancel Reservation 9. Log Out\nEnter your choice: ")

                            if customer_choice == '1':
                                print(customer_username)
                                customer_details = customer_service.get_customer_by_username(customer_username)
                                if customer_details:
                                    print("Customer Details:")
                                    print(f"ID: {customer_details[0]}")
                                    print(f"Name: {customer_details[1]}")
                                    print(f"Address: {customer_details[5]}")
                                    print(f"Phone: {customer_details[4]}")
                                    print(f"Email: {customer_details[3]}")
                                else:
                                    print("Customer not found!")


                            elif customer_choice == '2':
                                update_customer = {
                                    "customer_id": input("Enter the customer id to update: "),
                                    "first_name": input("Enter the first name to update: "),
                                    "last_name": input("Enter the last name to update: "),
                                    "email": input("Enter the email to update: "),
                                    "phone_number": input("Enter the phone_number to update: "),
                                    "address": input("Enter the address to update: "),
                                    "username": input("Enter the username to update: "),
                                    "password": input("Enter the password to update: ")
                                }
                                customer_service.update_customer(update_customer)
                                print("Customer updated successfully!")

                            elif customer_choice == '3':
                                customer_id = int(input("Enter the customer ID: "))
                                print("Enter your username and password to confirm deletion...!")
                                username = input("Enter your username:")
                                password = input("Enter your password :")
                                if authunticate_service.authenticate_user(username, password):
                                    customer_service.delete_customer(customer_id)
                                    print("Your details have been deleted successfully....")
                                else:
                                    print("Invalid username or password!!!")

                            elif customer_choice == '4':
                                vehicle_id = int(input("Enter the vehicle id: "))
                                try:
                                    details = vehicle_service.get_vehicle_by_id(vehicle_id)
                                    print("Model: ", details[1])
                                    print("Make: ", details[2])
                                    print("Year: ", details[3])
                                    print("Color: ", details[4])
                                    print("RegistrationNumber: ", details[5])
                                    print("Availability: ", details[6])
                                    print("DailyRate: ", details[7])
                                except VehicleNotFoundException as e:
                                    print(e)
                            elif customer_choice == '5':
                                res = vehicle_service.get_available_vehicles()
                                print("Available Vehicles: ")
                                for vehicles in res:
                                    print(vehicles)
                            elif customer_choice == '6':
                                reservation_data = {
                                    "CustomerID": input("Enter customer ID: "),
                                    "VehicleID": input("Enter Vehicle ID: "),
                                    "StartDate": date.today(),
                                    "EndDate": input("Enter EndDate: "),
                                    "TotalCost": input("Enter TotalCost: "),
                                    "Status": input("Enter Status: ")
                                }
                                try:
                                    reservation_service.create_reservation(reservation_data)
                                    print("Reservation Confirmed....")
                                except ReservationException as e:
                                    print(e)

                            elif customer_choice == '7':
                                update_reservation_data = {
                                    "ReservationID": input("Enter the reservation ID to be updated:"),
                                    "CustomerID": input("Enter customer ID: "),
                                    "VehicleID": input("Enter Vehicle ID: "),
                                    "StartDate": date.today(),
                                    "EndDate": input("Enter EndDate: "),
                                    "TotalCost": input("Enter TotalCost: "),
                                    "Status": input("Enter Status: ")
                                }

                                reservation_service.update_reservation(update_reservation_data)
                            elif customer_choice == '8':
                                res_id = input("Enter your reservation ID: ")
                                reservation_service.cancel_reservation(res_id)
                                print("Your reservation have been cancelled sucessfully....")

                            elif customer_choice == '9':
                                print("Logging out...\n")
                                break

                except AuthenticationException as e:
                    print(e)


            elif customer_auth_choice == '2':

                customer_details = {
                    'FirstName': input("Enter your First Name:"),
                    'LastName': input("Enter your Last Name:"),
                    'Email': input("Enter your Email:"),
                    'PhoneNumber': input("Enter your PhoneNumber:"),
                    'Address': input("Enter your Address:"),
                    'Username': input("Enter Username:"),
                    'Password': input("Enter your Password:"),
                    'RegistrationDate': date.today()
                }

                customer_service.register_customer(customer_details)
                print("Account created successfully!\n")

            elif customer_auth_choice == '3':

                print("Going back to main menu...\n")

            else:
                print("Invalid choice. Please enter a number between 1 and 3.\n")

        elif section_choice == '2':
            try:
                admin_username = input("Enter your username: ")
                admin_password = input("Enter your password: ")
                if authunticate_service.authenticate_admin(admin_username, admin_password):
                    print("Login Successfull...!!")
                    while True:
                        print("Admin Operations:")
                        admin_choice = input(
                            "1. View Your Profile\n2. Register New Admin\n3. Update Profile\n"
                            "4. Remove Account\n5. View Reservation Report\n"
                            "6. Add Vehicle \n7. Update Vehicle Details\n"
                            "8. Remove Vehicle \n9.Log Out\nEnter your choice(1-9): ")

                        if admin_choice == '1':
                            try:
                                details = admin_service.get_admin_by_username(admin_username)
                                print("Admin ID: ", details[0])
                                print("Name: ", details[1])
                                print("Email: ", details[3])
                                print("PhoneNumber: ", details[4])
                                print("Username: ", details[5])
                                print("Password: ", details[6])
                                print("Role: ", details[7])
                                print("Join Date: ", details[8])
                            except AdminNotFoundException as e:
                                print(e)




                        elif admin_choice == '2':

                            admin_details = {
                                'FirstName': input("Enter admin's First Name:"),
                                'LastName': input("Enter admin's Last Name:"),
                                'Email': input("Enter admin's Email:"),
                                'PhoneNumber': input("Enter admin's PhoneNumber:"),
                                'Username': input("Enter admin's Username:"),
                                'Password': input("Enter admin's Password:"),
                                'Role': input("Enter admin's Role:"),
                                'JoinDate': date.today()
                            }
                            admin_service.register_admin(admin_details)
                            print("Admin registration successful.")

                        elif admin_choice == '3':
                            update_details = {
                                'AdminID': input("Enter your ID to be updated:"),
                                'FirstName': input("Enter your First Name:"),
                                'LastName': input("Enter your Last Name:"),
                                'Email': input("Enter your Email:"),
                                'PhoneNumber': input("Enter your PhoneNumber:"),
                                'Username': input("Enter your Username:"),
                                'Password': input("Enter your Password:"),
                                'Role': input("Enter your Role:"),
                                'JoinDate': date.today()
                            }
                            admin_service.update_admin(update_details)
                            print("Updated Sucessfully....")

                        elif admin_choice == '4':
                            admin_id = input("Enter your ID : ")
                            admin_service.delete_admin(admin_id)
                            print("Admin removed!!!")

                        elif admin_choice == '5':
                            res_id = input("Enter the reservation ID:")
                            report.generate_report(res_id)

                        elif admin_choice == '6':
                            vehicle_details = {
                                "Model": input("Enter the model: "),
                                "Make": input("Enter the Make: "),
                                "Year": input("Enter the Year: "),
                                "Color": input("Enter the Color: "),
                                "RegistrationNumber": input("Enter the RegistrationNumber: "),
                                "Availability": input("Enter the Availability: "),
                                "DailyRate": input("Enter the DailyRate: ")

                            }
                            vehicle_service.add_vehicle(vehicle_details)
                            print("Vehicle added sucessfully...")

                        elif admin_choice == '7':
                            update_vehicle = {
                                "vehicle_id": input("Enter the vehicle id whose data to be updated: "),
                                "Model": input("Enter the model : "),
                                "Make": input("Enter the Make: "),
                                "Year": input("Enter the Year: "),
                                "Color": input("Enter the Color: "),
                                "RegistrationNumber": input("Enter the RegistrationNumber: "),
                                "Availability": input("Enter the Availability: "),
                                "DailyRate": input("Enter the DailyRate: ")

                            }
                            vehicle_service.update_vehicle(update_vehicle)
                            print("The vehicle datas have been updated successfully.....")

                        elif admin_choice == '8':
                            vehicle_id = int(input("Enter the vehicle ID: "))
                            vehicle_service.remove_vehicle(vehicle_id)
                            print("This vehicle have been removed sucessfully....")

                        elif admin_choice == '9':
                            print("Logged Out...!!")
                            break
            except AuthenticationException as e:
                print(e)


        elif section_choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

    db_context.connection.close()


if __name__ == "__main__":
    main()
