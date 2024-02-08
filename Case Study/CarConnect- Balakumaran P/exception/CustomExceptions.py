class AuthenticationException(Exception):
    def __str__(self):
        return "Incorrect username or password during customer or admin login."

class ReservationException(Exception):
    def __str__(self):
        return "Attempting to make a reservation for a vehicle that is already reserved."

class VehicleNotFoundException(Exception):
    def __str__(self):
        return "Trying to get details of a vehicle that does not exist."

class AdminNotFoundException(Exception):
    def __str__(self):
        return "Attempting to access details of an admin that does not exist"


class DatabaseConnectionException(Exception):
    def __str__(self):
        return 'Unable to establish a connection to the database.'
