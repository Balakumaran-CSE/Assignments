class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        host = "localhost"
        database = "CarConnect"
        user = "root"
        password = "root"

        connection_string = {
            "host": host,
            "database": database,
            "user": user,
            "password": password,
        }
        return connection_string