class InsufficientFundException(Exception):
    def __init__(self):
        super().__init__("You have Insufficient fund in your account.")

class InvalidAccountException(Exception):
    def __init__(self):
        super().__init__("User entered the invalid account number when tries to transfer amount")

class OverDraftLimitExcededException(Exception):
    def __init__(self):
        super().__init__("Over Draft limit exceeded..")