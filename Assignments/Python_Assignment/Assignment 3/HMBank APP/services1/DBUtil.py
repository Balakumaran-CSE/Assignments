import mysql.connector
class DBUtil:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', user='root', passwd='root', database='HMBank', port='3306')
        if self.con:
            print("Connection successful")

    def __del__(self):
        if hasattr(self, 'con') and self.con.is_connected():
            self.con.close()
            print("Connection closed")