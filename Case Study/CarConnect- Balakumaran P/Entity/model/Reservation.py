class Reservation:
    def __init__(self, reservationID, customerID, vehicleID, startDate, endDate, totalCost, status):
        self._reservationID = reservationID
        self._customerID = customerID
        self._vehicleID = vehicleID
        self._startDate = startDate
        self._endDate = endDate
        self._totalCost = totalCost
        self._status = status

    @property
    def reservationID(self):
        return self._reservationID

    @reservationID.setter
    def reservationID(self, value):
        self._reservationID = value

    @property
    def customerID(self):
        return self._customerID

    @customerID.setter
    def customerID(self, value):
        self._customerID = value

    @property
    def vehicleID(self):
        return self._vehicleID

    @vehicleID.setter
    def vehicleID(self, value):
        self._vehicleID = value

    @property
    def startDate(self):
        return self._startDate

    @startDate.setter
    def startDate(self, value):
        self._startDate = value

    @property
    def endDate(self):
        return self._endDate

    @endDate.setter
    def endDate(self, value):
        self._endDate = value

    @property
    def totalCost(self):
        return self._totalCost

    @totalCost.setter
    def totalCost(self, value):
        self._totalCost = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def calculateTotalCost(self):
        pass