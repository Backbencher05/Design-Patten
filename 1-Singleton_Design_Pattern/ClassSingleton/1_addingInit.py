class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print("Creating New Instance")
            cls.__instance = super().__new__(cls)
        else:
            print("Using Existing Instance")
        return cls.__instance
    
    def __init__(self):
        print("Running __init__")
        self.value = None

s1 = Singleton()
s1.value = 42
print("***")
s2 = Singleton()
print(s2.value)
print(s1 is s2)
