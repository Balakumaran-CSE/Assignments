from exception.CustomExceptions import AuthenticationException


class AuthenticationService:
    def __init__(self, database_context):
        self.db_context = database_context

    def authenticate_user(self, username, password):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT Username,Password FROM Customer WHERE Username = %s and Password = %s",
                    (username, password))
        res = cur.fetchone()
        if res is None:
            raise AuthenticationException
        return res is not None


    def authenticate_admin(self, username, password):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT UserName,Password FROM Admin WHERE Username = %s AND Password = %s",
                    (username, password))
        res = cur.fetchone()
        if res is None:
            raise AuthenticationException
        return res is not None
