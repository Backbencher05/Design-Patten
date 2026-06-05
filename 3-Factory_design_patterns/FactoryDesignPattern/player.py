"""
we have class Player and let player and attack so we have created attack function but
we have diff-diff player and every palyer haveit's own way to attack

so let's create player class as Abstract class and deoending on the requirement we we impliment 
the way player attack in it's respective class 
let's 
 - knight player attack method 
 - archer player attack method
"""


from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def attack(self):
        pass