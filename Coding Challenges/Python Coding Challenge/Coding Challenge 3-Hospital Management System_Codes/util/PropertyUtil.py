class PropertyUtil:
    @staticmethod
    def get_property_string(connection_details):
        connection_string = {
            'host': connection_details['host'],
            'user': connection_details['user'],
            'passwd': connection_details['passwd'],
            'port': connection_details['port'],
            'database': connection_details['dbname']  # Use 'database' instead of 'dbname'
        }

        return connection_string