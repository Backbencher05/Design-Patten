from .BankAdapter import BankAdapter
from Banks.IciciBank import IciciBank

class IciciBankAdapter(BankAdapter):

    def __init__(self):
        self.bank = IciciBank()
         
    def CheckBalance(self):
        # return IciciBank().bal()
        return self.bank.bal()