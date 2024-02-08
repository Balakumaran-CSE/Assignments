class Customer:
    def __init__(self, customerID, firstName, lastName, email, phoneNumber, address, username, password,
                 registrationDate):
        self._customerID = customerID
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._phoneNumber = phoneNumber
        self._address = address
        self._username = username
        self._password = password
        self._registrationDate = registrationDate

    @property
    def customerID(self):
        return self._customerID

    @customerID.setter
    def customerID(self, value):
        self._customerID = value

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        self._firstName = value

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        self._phoneNumber = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def registrationDate(self):
        return self._registrationDate

    @registrationDate.setter
    def registrationDate(self, value):
        self._registrationDate = value

    def authenticate(self, enteredPassword):
        return self._password == enteredPassword