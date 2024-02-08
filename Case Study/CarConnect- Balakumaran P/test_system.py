import unittest
from datetime import date

from dao.service.AuthenticationService import AuthenticationService
from dao.service.CustomerService import CustomerService
from dao.service.DatabaseContext import DatabaseContext
from dao.service.VehicleService import VehicleService
from exception.CustomExceptions import AuthenticationException

from util.DBPropertyUtil import DBPropertyUtil
from util.DBConnUtil import DBConnUtil

class TestCustomerAuthentication(unittest.TestCase):
    def setUp(self):
        self.db_context = DatabaseContext()
        self.db_context.connect()
        self.auth_service = AuthenticationService(self.db_context)
        self.customer_service = CustomerService(self.db_context)
        self.existing_customer_id = 1
        self.existing_vehicle_id = 1
        self.vehicle_service = VehicleService(self.db_context)
    def tearDown(self):
        try:
            if self.db_context:
                self.db_context.connection.close()
        except Exception as e:
            print(f"Error closing database connection: {e}")

    def test_invalid_credentials(self):
        invalid_username = "invalid_username"
        invalid_password = "invalid_password"

        with self.assertRaises(AuthenticationException) as context:
            self.auth_service.authenticate_user(invalid_username, invalid_password)

        self.assertEqual(str(context.exception), "Incorrect username or password during customer or admin login.")

    def test_update_customer_information(self):

        updated_info = {
            'customer_id': self.existing_customer_id,
            'first_name': 'Balakumaran',
            'last_name': 'P',
            'email': 'balabkkumaran55@gmail.com',
            'phone_number': '6382474871',
            'address': 'Pondicherry',
            'username': 'mr_bala_bk_45',
            'password': 'prathibala5'
        }
        self.customer_service.update_customer(updated_info)
        updated_customer = self.customer_service.get_customer_by_id(self.existing_customer_id)
        self.assertEqual(updated_customer[1], 'Balakumaran')
        self.assertEqual(updated_customer[2], 'P')
        self.assertEqual(updated_customer[3], 'balabkkumaran55@gmail.com')
        self.assertEqual(updated_customer[4], '6382474871')
        self.assertEqual(updated_customer[5], 'Pondicherry')
        self.assertEqual(updated_customer[6], 'mr_bala_bk_45')
        self.assertEqual(updated_customer[7], 'prathibala5')

    def test_update_vehicle(self):
        updated_info = {
            'vehicle_id': self.existing_vehicle_id,
            'Model': 'Aadi',
            'Make': 'Tata',
            'Year': '2023',
            'Color': 'Blue',
            'RegistrationNumber': 'PY7282',
            'Availability': 0,
            'DailyRate': '1555.00'
        }
        self.vehicle_service.update_vehicle(updated_info)

        updated_vehicle = self.vehicle_service.get_vehicle_by_id(self.existing_vehicle_id)

        self.assertEqual(updated_vehicle[1], 'Aadi')
        self.assertEqual(updated_vehicle[2], 'Tata')
        self.assertEqual(updated_vehicle[3], 2023)
        self.assertEqual(updated_vehicle[4], 'Blue')
        self.assertEqual(updated_vehicle[5], 'PY7282')
        self.assertEqual(updated_vehicle[6], 0)
        self.assertEqual(updated_vehicle[7], 1555.00)

    def test_all_vehicles(self):
        connection = self.db_context.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Vehicle")
        all_vehicles = cursor.fetchall()

        self.assertIsNotNone(all_vehicles, "The list of all vehicles should not be None.")
        self.assertIsInstance(all_vehicles, list, "The result should be a list.")
        self.assertGreater(len(all_vehicles), 0, "There should be at least one vehicle in the list.")

    def test_available_vehicles(self):
        connection = self.db_context.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Vehicle WHERE Availability = 1")
        available_vehicles = cursor.fetchall()
        for vehicle in available_vehicles:
            self.assertEqual(vehicle[6], 1, "The 'Availability' should be 1 for available vehicles.")


if __name__ == '__main__':
    unittest.main()
