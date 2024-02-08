import mysql.connector

from exception.CustomExceptions import DatabaseConnectionException


class DBConnUtil:
    @staticmethod
    def get_connection(connection_string):
        try:
            connection = mysql.connector.connect(**connection_string)
        except DatabaseConnectionException as e:
            print(e)
        return connection

