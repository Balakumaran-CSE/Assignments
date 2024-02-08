class ReportGenerator:
    def __init__(self, database_context):
        self.db_context = database_context

    def generate_report(self,res_id):
        connection = self.db_context.get_connection()
        cursor = connection.cursor()

        query = "SELECT r.ReservationID, r.CustomerID, r.VehicleID, r.StartDate, r.EndDate, r.TotalCost, r.Status, " \
                "v.Model, v.Make, v.Year, v.Color, v.RegistrationNumber, v.Availability, v.DailyRate " \
                "FROM Reservation r JOIN Vehicle v ON r.VehicleID = v.VehicleID WHERE r.ReservationID = %s"

        cursor.execute(query,(res_id,))
        combined_data = cursor.fetchall()

        print("Report:")
        for entry in combined_data:
            print(f"Reservation ID: {entry[0]}")
            print(f"Customer ID: {entry[1]}")
            print(f"Vehicle ID: {entry[2]}")
            print(f"Start Date: {entry[3]}")
            print(f"End Date: {entry[4]}")
            print(f"Total Cost: {entry[5]}")
            print(f"Status: {entry[6]}")
            print(f"Model: {entry[7]}")
            print(f"Make: {entry[8]}")
            print(f"Year: {entry[9]}")
            print(f"Color: {entry[10]}")
            print(f"Registration Number: {entry[11]}")
            print(f"Availability: {entry[12]}")
            print(f"Daily Rate: {entry[13]}")
            print("\n")


