from datetime import datetime

from bean1.Account import CurrentAccount, SavingsAccount
from bean1.ICustomerServiceProvider import ICustomerServiceProvider
from bean1.Transaction import Transaction


class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts={}
        self.transactions=[]

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].balance
        else:
            return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance+=amount
            transaction=Transaction(self.accounts[account_number],'Deposit',datetime.now(),amount)
            self.transactions.append(transaction)
            print(f"Deposited an amount of {amount}")
            return self.accounts[account_number].balance
        return None

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            account=self.accounts[account_number]

            if isinstance(account,SavingsAccount) and account.balance-amount<500:
                print("Insufficient fund in your account")
            elif isinstance(account,CurrentAccount) and account.balance+account.overdrafted_limit<amount:
                print("Insufficient fund in your account")
            else:
                account.balance-=amount
                transaction=Transaction(account,'Withdraw',datetime.now(),amount)
                self.transactions.append(transaction)
                return account.balance
        return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_balance = self.get_account_balance(from_account_number)
        if from_balance is not None and from_balance >= amount:
            self.withdraw(from_account_number, amount)
            to_balance = self.deposit(to_account_number, amount)
            transaction=Transaction(self.accounts[from_account_number],'Tranfer- Sending Amount',datetime.now(),amount)
            self.transactions.append(transaction)
            transaction1=Transaction(self.accounts[to_account_number], 'Tranfer- Receive Amount', datetime.now(),
                                      amount)
            self.transactions.append(transaction1)
            if to_balance is not None:
                return to_balance
        print("Error: Insufficient funds for transfer.")
        return None

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return None

    def get_transactions(self, account_number, from_date, to_date):
        if account_number in self.accounts:
            account_transactions = [transaction for transaction in self.transactions
                                     if transaction.account.account_number == account_number
                                     and from_date <= transaction.date_time <= to_date]
            return account_transactions
        else:
            return None
