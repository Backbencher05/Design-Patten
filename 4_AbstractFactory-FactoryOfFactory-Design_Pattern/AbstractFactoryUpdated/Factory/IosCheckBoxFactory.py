from FactoryABC import Factory
from UIElements.iosCheckBox import IosCheckBox

class IosCheckBoxFactory(Factory):
    def create(self):
        return IosCheckBox