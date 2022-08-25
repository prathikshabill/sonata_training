class Account:
    def __init__(self,acno,name,type,balance):
        self.accountno=acno
        self.name=name
        self.type=type
        self.balance=balance

    def withdraw(self,balance,amount):
        if(balance<amount):
            raise LowBalanceException("Insufficient Balance")
        balance=balance-amount
        return balance

acc=Account("121","PRAT","SAVINGS",5000)



