class Admin:
    def __init__(self, adminID, firstName, lastName, email, phoneNumber, username, password, role, joinDate):
        self._adminID = adminID
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._phoneNumber = phoneNumber
        self._username = username
        self._password = password
        self._role = role
        self._joinDate = joinDate

    @property
    def adminID(self):
        return self._adminID

    @adminID.setter
    def adminID(self, value):
        self._adminID = value

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
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    @property
    def joinDate(self):
        return self._joinDate

    @joinDate.setter
    def joinDate(self, value):
        self._joinDate = value

    def authenticate(self, enteredPassword):
        return self._password == enteredPassword