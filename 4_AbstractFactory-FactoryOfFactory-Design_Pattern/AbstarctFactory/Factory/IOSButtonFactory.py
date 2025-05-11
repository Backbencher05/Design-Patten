from FactoryABC import Factory
from UIElements.iosButton import IosButton

class IosButtonFactory(Factory):
    def create(self):
        return IosButton()