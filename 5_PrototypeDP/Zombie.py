from monster import Monster
import copy

class Zombie(Monster):
    
    # let Zombie have some health given by user/ we can set some default health 
    def __init__(self, health):
        self.health = health

    def attack(self):
        print("Attacking")

    def clone(self):
        return copy.deepcopy(self)