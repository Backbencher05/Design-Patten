from FactoryABC import Factory
from UIElements.androidButton import AndriodButton

class AndroidButtonFactory(Factory):
    def create(self):
        return  AndriodButton()