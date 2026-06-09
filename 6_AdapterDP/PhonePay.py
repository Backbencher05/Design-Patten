# phone pay will call Adapters
class PhonePay:

    def __init__(self,Adapter):
        self.BankAdapter = Adapter

    
    def checkBalance(self):
        return self.BankAdapter.CheckBalance()