from .BankAdapter import BankAdapter
from Banks.YesBank import YesBank

class YesBankAdapter(BankAdapter):

    def __init__(self):
        self.bank = YesBank()
         
    def CheckBalance(self):
        # return IciciBank().bal()
        return self.bank.balance()