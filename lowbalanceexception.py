class LowBalanceException(Exception):
    def __init__(self,display):
        self.display=display

    def ammount(self):
        return self.display

