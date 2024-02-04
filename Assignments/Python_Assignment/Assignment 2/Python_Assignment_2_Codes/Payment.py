from Student import Student
class Payment(Student):
    def __init__(self, Payment_ID=None, Student_ID=None, Amount=None, Payment_Date=None):
        self.Payment_ID = Payment_ID
        Student.__init__(self, Student_ID)
        self.Amount = Amount
        self.Payment_Date = Payment_Date

    def GetStudent(self):
        print(f"{self.Student_ID} has made the payment")

    def GetPaymentAmount(self):
        print(f"Payment of {self.Amount} has been made")

    def GetPaymentDate(self):
        print(f"The Payment was made on {self.Payment_Date} ")