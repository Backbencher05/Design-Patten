from factory import Knight
from factory import Archer

# this CharacterFactory file  is also called practicle factory 

# if condition lie on the factory not in cient side 

class CharacterFactory:
    def create_player(self, player_type):
        if player_type == 'Knight':
            return Knight()
        
        if player_type == 'Archer':
            return Archer()