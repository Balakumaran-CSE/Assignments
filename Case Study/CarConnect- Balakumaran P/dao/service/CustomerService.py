from dao.service.ICustomerService import ICustomerService


class CustomerService(ICustomerService):
    def __init__(self, database_context):
        self.db_context = database_context

    def generate_customer_id(self):
        self.db_context.connect()
        connection = self.db_context.get_connection()

        cur = connection.cursor()
        cur.execute("SELECT MAX(CustomerID) FROM Customer")
        customer_id = cur.fetchone()[0]
        if customer_id is None:
            customer_id = 1
        else:
            customer_id += 1
        return customer_id

    def get_customer_by_id(self, customer_id):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM Customer WHERE CustomerID = %s", (customer_id,))
        res = cur.fetchone()
        return res

    def get_customer_by_username(self, username):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM Customer WHERE Username = %s", (username,))
        res = cur.fetchone()
        return res

    def register_customer(self, customer_data):
        connection = self.db_context.get_connection()
        customer_id = self.generate_customer_id()
        cur = connection.cursor()
        cur.execute(
            "INSERT INTO Customer "
            "(CustomerID, FirstName, LastName, Email, PhoneNumber, Address, Username, Password, "
            "RegistrationDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (customer_id, customer_data['FirstName'], customer_data['LastName'], customer_data['Email'],
             customer_data['PhoneNumber'], customer_data['Address'], customer_data['Username'],
             customer_data['Password'], customer_data['RegistrationDate'])
        )
        connection.commit()
        print("Customer registration successful...")

    def update_customer(self, customer_data):
        connection = self.db_context.get_connection()
        cur = connection.cursor()

        customer_id = customer_data.get("customer_id")
        first_name = customer_data.get("first_name")
        last_name = customer_data.get("last_name")
        email = customer_data.get("email")
        phone_number = customer_data.get("phone_number")
        address = customer_data.get("address")
        username = customer_data.get("username")
        password = customer_data.get("password")

        update_query = """
            UPDATE Customer
            SET
                FirstName = %s,
                LastName = %s,
                Email = %s,
                PhoneNumber = %s,
                Address = %s,
                Username = %s,
                Password = %s
            WHERE
                CustomerID = %s
        """
        cur.execute(update_query,
                    (first_name, last_name, email, phone_number, address, username, password, customer_id))
        connection.commit()

    def delete_customer(self, customer_id):
        connection = self.db_context.get_connection()
        cur = connection.cursor()
        cur.execute("DELETE FROM Customer WHERE CustomerID = %s", (customer_id,))
        connection.commit()
