from FactoryABC import Factory
from UIElements.androidCheckbox import AndroidCheckBox

class AndroidCheckBoxFactory(Factory):
    def create(self):
        return AndroidCheckBox()