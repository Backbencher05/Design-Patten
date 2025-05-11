from abc import ABC, abstractmethod
from Factory import AndroidButtonFactory, AndroidCheckBoxFactory, IOSButtonFactory, IosCheckBoxFactory

class AbstractAndroidFactory:
    def create_button(self):
        return AndroidButtonFactory()
    
    def create_checkbox(self):
        return AndroidCheckBoxFactory()
    

class AbstractIosFactory:
    def create_button(self):
        return IOSButtonFactory()
    
    def create_checkbox(self):
        return IosCheckBoxFactory()



"""
create abstractFactory as abstract and impliment it in 
- AbstractAndroidFactory
- AbstractIosFactory
"""

# class AbstractFactory(ABC):
#     @abstractmethod
#     def create_button(self):
#         pass

#     @abstractmethod
#     def create_checkbox(self):
#         pass

# class AbstractAndroidFactory(AbstractFactory):
#     def create_button(self):
#         return AndroidButtonFactory()
    
#     def create_checkbox(self):
#         return AndroidCheckBoxFactory
    

# class AbstractIosFactory(AbstractFactory):
#     def create_button(self):
#         return IOSButtonFactory()
    
#     def create_checkbox(self):
#         return IosCheckBoxFactory