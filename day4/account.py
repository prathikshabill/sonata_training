class Account:
    def __init__(self,accNumber,name,type,balance):
        self.AccountNumber = accNumber
        self.Name =name
        self.Type = type
        self.Balance =balance
    def withDraw(self,amount):
        if(self.Balance<amount):
            raise LowBalanceException("Insufficient Balance")
