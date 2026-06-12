class Server:
    # there can be multiple observer so let store them in the list/dict 
    def __init__(self):
        self.observers = []

    # In sever we have to register/ unregister the observer 
    # we have to take observer as input i.e which observer have to register 
    # this register and  unregister method call by oberser to register themself to server  
    def register(self,observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    # let server need to notify to observers when somthing chaanges happens

    def notify(self, temp, hum):
        for observer in self.observers:
            observer.update(temp, hum)  # every observer will have this update() method 
                                        # for now we have 2 parameter temp. and hum.


    # now we will have comcreate class of server for now let we have 
    # - weatherStation
    # write now we have created normal server class , we can create as ABC as well 