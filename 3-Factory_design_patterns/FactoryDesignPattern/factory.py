from knight import Knight
from archer import Archer
from abc import ABC, abstractmethod
from knight import KnightV2
"""
class KnightFactory:
    def createKnight(self):
        return Knight() # return object of knight
    

class ArcherFactory:
    def create(self):
        return Archer()
"""

"""
but how client will know while calling Knight player they have to call createKnight() method 
and while calling Archer player they have to call create() method 
it will create the confusion...
so they should be contract for that we have to use "Abstract Class"

- create PlayerFactory as abstract class, ensure to  have same method only let "create player"/ "call_player"
Note: - we can also create on new file as well 
        - in one file PlayerFactory as Abstract class 
        - in another file PlayerFactory class Implimentation in child class 
"""


class PlayerFactory(ABC):
    @abstractmethod
    def create_player(self):
        pass


class KnightFactory(PlayerFactory):
    def create_player(self):
        # return Knight()
    # if new version of night come we just have to update here, client don't have to care 
        return KnightV2()
    
class ArcherFactory(PlayerFactory):
    def create_player(self):
        return Archer()
    

# now , player have contoll/maintain the factory to this factory 
