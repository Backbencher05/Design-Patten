# let he want knight player 
from factory import KnightFactory

def get_player(player_val):
    if player_val == 'Knight':
        return KnightFactory().create_player().attack()
    
# let in future player knight have version2 we don't have to care
# client don't know which object is coming or latest code as code (loosly coupled)
# same as we have seen the app, home page/UI changed completely 

# Now here,
# we have solved to problem of version updation, 
# we have to solve OCP and SRP principle 
"""
Note:
but if are importing dirctly factories hare we have to change at multiple places
- importing dirctly factories here
- lot of changes
- lot of if else are there
"""

"""

so don't write if and else in your client code
delgate this work also to factory, as the work of factory is to create object

- create new factory, 
        - characterFactory (based on if else in will deside)
                        check the updated code of factory
""" 

if __name__ == '__main__':
    get_player('Knight')
