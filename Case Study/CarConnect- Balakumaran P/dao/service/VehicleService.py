from dao.service.IVehicleService import IVehicleService
from exception.CustomExceptions import VehicleNotFoundException


class VehicleService(IVehicleService):
    def __init__(self, database_context):
        self.db_context = database_context

    def generate_vehicle_id(self):
        self.db_context.connect()
        connection = self.db_context.get_connection()

        cur = connection.cursor()
        cur.execute("SELECT MAX(VehicleID) FROM Vehicle")
        max_vehicle_id = cur.fetchone()[0]
        if max_vehicle_id is None:
            return 1
        else:
            return max_vehicle_id + 1

    def get_vehicle_by_id(self, vehicle_id):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM Vehicle WHERE VehicleID = %s", (vehicle_id,))
        vehicle = cur.fetchone()
        connection.commit()
        if not vehicle:
            raise VehicleNotFoundException
        return vehicle

    def get_available_vehicles(self):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM Vehicle WHERE Availability = 1")
        res = cur.fetchall()
        return res

    def add_vehicle(self, vehicle_data):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        vehicle_id = self.generate_vehicle_id()
        cur.execute("INSERT INTO Vehicle VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    , (vehicle_id, vehicle_data['Model'], vehicle_data['Make'],
                       vehicle_data['Year'], vehicle_data['Color'], vehicle_data['RegistrationNumber'],
                       vehicle_data['Availability'], vehicle_data['DailyRate']))
        connection.commit()
        return vehicle_id

    def update_vehicle(self, vehicle_data):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        vehicle_id=vehicle_data.get('vehicle_id')
        model = vehicle_data.get('Model')
        make = vehicle_data.get('Make')
        year = vehicle_data.get('Year')
        color = vehicle_data.get('Color')
        reg_no = vehicle_data.get('RegistrationNumber')
        avl = vehicle_data.get('Availability')
        daily_rate = vehicle_data.get('DailyRate')
        cur.execute('''  
            UPDATE Vehicle
            SET Model = %s,
                Make = %s,
                Year = %s,
                Color = %s,
                RegistrationNumber = %s,
                Availability = %s,
                DailyRate = %s   
            WHERE VehicleID = %s
            ''',
                    (model, make, year, color, reg_no, avl, daily_rate, vehicle_id))
        connection.commit()

    def remove_vehicle(self, vehicle_id):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("DELETE FROM Vehicle WHERE VehicleID = %s", (vehicle_id,))
        connection.commit()

