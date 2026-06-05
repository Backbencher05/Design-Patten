from abc import ABC, abstractmethod



# we can have diff-diff Monster 
# - Zombie
# - Goblin
# - arc etc etc

# so we will create and abstract class and it's implimention done by its child class 

class Monster(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def clone(self):
        pass