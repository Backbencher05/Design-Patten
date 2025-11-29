class Singleton:
    _instance = None 
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(Singleton,cls).__new__(cls)

        return cls._instance
    
if __name__ == "__main__":
    instance1 = Singleton()
    print(instance1)
    instance2 = Singleton()
    print(instance1 is instance2) # True

# we can use both
# - cls._instance = super(Singleton,cls).__new__(cls)
# - cls._instance = super().__new__(cls)

class Singleton:
    _instance = None 
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)

        return cls._instance
    
if __name__ == "__main__":
    instance1 = Singleton()
    print(instance1)
    instance2 = Singleton()
    print(instance1 is instance2) # True