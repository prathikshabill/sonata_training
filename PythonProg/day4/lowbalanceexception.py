class LowBalanceException(Exception):
    def __init__(self,message):
        self.Message = message
    def lowbalance(self):
        return self.Message