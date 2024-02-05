from abc import ABC,abstractmethod
class IBankRepository(ABC):

    @abstractmethod
    def createAccount(self,con,customer,account_type,balance):
        pass
    @abstractmethod
    def listAccount(self,con):
        pass
    @abstractmethod
    def calculateInterest(self, con, user_interest_rate):
        pass
    @abstractmethod
    def getAccountBalance(self,con,account_number):
        pass
    @abstractmethod
    def createCustomer(self,con, first_name, last_name,DOB,email,phone_no,address ):
        pass
    @abstractmethod
    def deposit(self,con,account_number,amount):
        pass
    @abstractmethod
    def withdraw(self,con,account_number,amount):
        pass
    @abstractmethod
    def transfer(self,con,from_account_number,to_account_number,amount):
        pass
    @abstractmethod
    def getAccountdetails(self,con,account_number):
        pass
    @abstractmethod
    def getTransactions(self,con,account_number,from_date,to_date):
        pass
    @abstractmethod
    def generateCustomerId(self,con):
        pass