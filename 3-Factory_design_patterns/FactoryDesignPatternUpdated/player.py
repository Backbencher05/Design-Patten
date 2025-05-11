from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def attack(self):
        pass