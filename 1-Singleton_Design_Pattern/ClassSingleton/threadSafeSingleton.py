import threading

class Singleton:
    __instance = None
    __lock = threading.Lock() # create at class level

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(Singleton,cls).__new__(cls)

        return cls.__instance

if __name__ == "__main__":
    instance = Singleton()
    print(instance)
    instance2 = Singleton()
    print(instance2)
    print(instance is instance2)