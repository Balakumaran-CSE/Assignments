from dao.service.IAdminService import IAdminService
from exception.CustomExceptions import AdminNotFoundException


class AdminService(IAdminService):
    def __init__(self,database_context):
        self.database_context=database_context
    def generate_admin_id(self):
        connection=self.database_context.get_connection()
        cur=connection.cursor()
        cur.execute("SELECT MAX(AdminID) FROM Admin")
        admin_id=cur.fetchone()[0]
        if admin_id is None:
            admin_id=1
        else:
            admin_id+=1
        return admin_id

    def get_admin_by_username(self, username):
        con=self.database_context.get_connection()
        cur=con.cursor()
        cur.execute("SELECT * FROM Admin WHERE username = %s",(username,))
        res=cur.fetchone()
        if res is None:
            raise AdminNotFoundException
        return res
    def get_admin_by_id(self, admin_id):
        con = self.database_context.get_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM Admin WHERE username = %s", (admin_id,))
        res = cur.fetchone()

        return res
    def register_admin(self, admin_data):
        connection = self.database_context.get_connection()
        cur = connection.cursor()
        admin_id = self.generate_admin_id()
        cur.execute("INSERT INTO Admin VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    , (admin_id, admin_data['FirstName'], admin_data['LastName'],
                       admin_data['Email'], admin_data['PhoneNumber'], admin_data['Username'],
                       admin_data['Password'],admin_data['Role'],admin_data['JoinDate']))
        connection.commit()

    def update_admin(self, admin_data):
        connection = self.database_context.get_connection()
        cur = connection.cursor()
        AdminID=admin_data.get('AdminID')
        FirstName = admin_data.get('FirstName')
        LastName = admin_data.get('LastName')
        Email = admin_data.get('Email')
        PhoneNumber = admin_data.get('PhoneNumber')
        Username = admin_data.get('Username')
        Password = admin_data.get('Password')
        Role = admin_data.get('Role')
        JoinDate = admin_data.get('JoinDate')

        cur.execute('''  
            UPDATE Admin
            SET FirstName = %s,
                LastName = %s,
                Email = %s,
                PhoneNumber = %s,
                Username = %s,
                Password = %s,
                Role = %s,
                JoinDate = %s
            WHERE 
                AdminID = %s
        ''', (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate, AdminID))

        connection.commit()


    def delete_admin(self, admin_id):
        con=self.database_context.get_connection()
        cur=con.cursor()
        cur.execute("DELETE FROM Admin WHERE AdminID = %s", (admin_id,))
        con.commit()
