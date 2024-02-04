from abc import ABC,abstractmethod
class IBankServiceProvider(ABC):

    @abstractmethod
    def create_account(self,customer,account_number,account_type,balance):
        pass

    @abstractmethod
    def lisAccounts(self):
        pass

    @abstractmethod
    def getAccountDetails(self,account_number):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass