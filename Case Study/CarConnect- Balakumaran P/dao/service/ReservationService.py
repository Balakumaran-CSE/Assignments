from dao.service.IReservationService import IReservationService
from exception.CustomExceptions import ReservationException


class ReservationService(IReservationService):
    def __init__(self, database_context):
        self.db_context = database_context

    def generate_reservation_id(self):
        self.db_context.connect()
        connection = self.db_context.get_connection()

        cur = connection.cursor()
        cur.execute("SELECT MAX(ReservationID) FROM Reservation")
        reservation_id = cur.fetchone()[0]
        if reservation_id is None:
            reservation_id = 1
        else:
            reservation_id += 1
        return reservation_id

    def get_reservation_by_id(self, reservation_id):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM Reservation WHERE ReservationID = %s", (reservation_id,))
        res = cur.fetchone()
        return res

    def get_reservations_by_customer_id(self, customer_id):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM Reservation WHERE CustomerID = %s", (customer_id,))
        res = cur.fetchall()
        return res

    def create_reservation(self, reservation_data):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT COUNT(*) FROM Reservation WHERE VehicleID = %s", (reservation_data['VehicleID'],))
        count = cur.fetchone()[0]

        if count > 0:
            raise ReservationException("Attempting to make a reservation for a vehicle that is already reserved.")
        else:
            res_id = self.generate_reservation_id()
            cur.execute("INSERT INTO Reservation VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (res_id, reservation_data['CustomerID'], reservation_data['VehicleID'],
                         reservation_data['StartDate'], reservation_data['EndDate'], reservation_data['TotalCost'],
                         reservation_data['Status']))
            connection.commit()

    def update_reservation(self, reservation_data):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        res_id = reservation_data.get('ReservationID')
        CustomerID = reservation_data.get('CustomerID')
        VehicleID = reservation_data.get('VehicleID')
        StartDate = reservation_data.get('StartDate')
        EndDate = reservation_data.get('EndDate')
        TotalCost = reservation_data.get('TotalCost')
        Status = reservation_data.get('Status')

        cur.execute('''
                    UPDATE Reservation
                    SET CustomerID = %s,
                        VehicleID = %s,
                        StartDate = %s,
                        EndDate = %s,
                        TotalCost = %s,
                        Status = %s
                    WHERE ReservationID = %s
                    ''',
                    (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status, res_id))

        connection.commit()
        print("Updated successfully....")

    def cancel_reservation(self, reservation_id):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("DELETE FROM Reservation WHERE ReservationID = %s", (reservation_id,))
        connection.commit()
