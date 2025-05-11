from CharacterFactory import CharacterFactory


def create_player(val_from_player):
    player = CharacterFactory().create_player(val_from_player)
    player.attack()

"""
so don't write if and else in your client code
delgate this work also to factory, as the work of factory is to create object

- create new factory, 
        - characterFactory (based on if else in will deside)
                       
""" 


"""
# let in future player knight have version2 we don't have to care
# client don't knw which object is coming or latest code as code (loosly coupled)
# same as we have seen the app, home page/UI changed completely 

we have to solved

- problem of version updation, 
- OCP and SRP principle 
- importing dirctly factories, change at multiple places
- importing dirctly factories here
- lot of changes
- lot of if else are there
"""






if __name__ == '__main__':
    create_player("Knight")