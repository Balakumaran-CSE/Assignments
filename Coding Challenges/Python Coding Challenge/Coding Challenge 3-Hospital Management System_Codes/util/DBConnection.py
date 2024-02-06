import mysql.connector
from util.PropertyUtil import PropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def get_connection(connection_details):
        if DBConnection.connection is None:
            connection_string = PropertyUtil.get_property_string(connection_details)
            DBConnection.connection = mysql.connector.connect(**connection_string)

        return DBConnection.connection