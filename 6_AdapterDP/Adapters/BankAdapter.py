from abc import ABC, abstractmethod

class BankAdapter(ABC):
    @abstractmethod
    def CheckBalance(self):
        pass