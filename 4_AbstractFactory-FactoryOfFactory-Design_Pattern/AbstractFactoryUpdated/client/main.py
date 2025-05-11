from Factory.AbstractFactory import AbstractAndroidFactory, AbstractIosFactory
from Factory.OSFactory import OSFactory

def Deploy(val):
    abs = OSFactory("An")

# let in future  have version2 we don't have to care
# client don't knw which object is coming or latest code as code (loosly coupled)
# same as we have seen the app, home page/UI changed completely 

# we have solved to problem of version updation, 
# we have to solve OCP and SRP principle 
"""
Note:
but if are importing dirctly factories hare we have to change at multiple places
- importing dirctly factories here
- lot of changes
- lot of if else are there
"""


if __name__ == '__main__':
    Deploy('ANDROID')