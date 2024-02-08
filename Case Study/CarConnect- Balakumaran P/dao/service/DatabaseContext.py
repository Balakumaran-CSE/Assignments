from exception.CustomExceptions import DatabaseConnectionException
from util.DBConnUtil import DBConnUtil
from util.DBPropertyUtil import DBPropertyUtil

class DatabaseContext:
    def __init__(self):
        self.connection_string = DBPropertyUtil.get_connection_string()
        self.connection = None

    def connect(self):
        try:
            self.connection = DBConnUtil.get_connection(self.connection_string)
        except DatabaseConnectionException as e:
            print(e)

    def get_connection(self):
        return self.connection
