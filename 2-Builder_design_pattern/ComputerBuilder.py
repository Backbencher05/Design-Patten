# Director call the builder 
"""
here we are building different types of computer like we have
    - Gaming Computer 
    - Office Computer 
    - home computer 
depending on the requirement from the builder(have requirement from the user/main() file) 
we will build that type of computer 

so, 
    let make this Computer builder as "abstract class" becuase depending on the requirement we need to build the computer 
and diffent type of computers are responsible for implimentation i.e child class
    """

from abc import ABC, abstractmethod
class ComputerBuilder(ABC):
    
    @abstractmethod
    def set_cpu(self,cpu):
        pass

    @abstractmethod
    def set_gpu(self,gpu):
        pass

    @abstractmethod
    def set_ram(self,ram):
        pass

    @abstractmethod
    def set_storage(self,storage):
        pass

    @abstractmethod
    def set_power_supply(self,power_supply):
        pass

    # we also need one extra method to build the computer , it will return the computer object
    @abstractmethod
    def build(self):
        pass

