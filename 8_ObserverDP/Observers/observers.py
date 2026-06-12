
# Obervers have to register themself to the server that i am your observer
from abc import ABC, abstractmethod
from servers.server import Server

class Observer(ABC):

    def registerSubject(self, server):
        server.register(self) # register() method present in the server so that observer can register themself

    def unregisterSubject(self, server):
        server.unregister(self)  # unregister() method present in the server so that observer can unregister themself

    # they will recive let temp. and humandity from server/subject 
    @abstractmethod
    def update(self, temp, humidity):
        pass
