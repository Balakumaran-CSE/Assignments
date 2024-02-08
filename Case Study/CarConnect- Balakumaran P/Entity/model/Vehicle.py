class Vehicle:
    def __init__(self, vehicleID, model, make, year, color, registrationNumber, availability, dailyRate):
        self._vehicleID = vehicleID
        self._model = model
        self._make = make
        self._year = year
        self._color = color
        self._registrationNumber = registrationNumber
        self._availability = availability
        self._dailyRate = dailyRate

    @property
    def vehicleID(self):
        return self._vehicleID

    @vehicleID.setter
    def vehicleID(self, value):
        self._vehicleID = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def registrationNumber(self):
        return self._registrationNumber

    @registrationNumber.setter
    def registrationNumber(self, value):
        self._registrationNumber = value

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, value):
        self._availability = value

    @property
    def dailyRate(self):
        return self._dailyRate

    @dailyRate.setter
    def dailyRate(self, value):
        self._dailyRate = value