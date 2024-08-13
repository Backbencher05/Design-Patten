class Singleton:
    __instance = None #private: initially when we create class we don't have any object of this class
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: # i.e no object , means we have to create object
            cls.__instance = super(Singleton,cls).__new__(cls)
        return cls.__instance


if __name__ == "__main__":
    instance = Singleton() # __new__() method will trigger before __init__, as write now it's None at very
                            # first call of __new__, it will create the object and assign it to the __instance variable
                            #  and return the instance
    print(instance)
    instance2 = Singleton()
    print(instance2)
    print(instance is instance2)

