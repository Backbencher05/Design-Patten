from GamingComputerBuilder import GamingComputerBuilder
from HomeComputerBuilder import HomeComputerBuilder
from ComputerDirector import ComputerDirector


if __name__ == '__main__':
    """
        I want gaming Computer, let's create builder for that, 
    shall i call build() method directly from here ?
    No,I will
     assign a dirctor to build the computer 
    """
# I want gaming Computer
    gb = GamingComputerBuilder()
    """
    shall i call build() method directly from here present inside GamingComputerBuilder class ?
    No,
    I will assign a dirctor to build the computer 
    """
    # hb = HomeComputerBuilder()#let i need Home computer 
    # requirement go to director , we will pass our requirement by passing values in the arguments
    # right now we are passing directly 
    director = ComputerDirector(gb)
    # director tell the builder to construct 
    director.construct()
    # after construction done get the computer and give to the user
    c = director.get_computer()
    print(c)