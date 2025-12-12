import threading

class Singleton:
    __instance = None
    __lock = threading.Lock() # create at class level
    # we have to use mutex(acting as lock), that only one thread can access a resource at a time

    def __new__(cls, *args, **kwargs):
        with cls.__lock: # using "with lock", lock automatically release the lock one the indentation/code execute i.e before return
            if cls.__instance is None: #  # as lock condition will slow down out process, 
                cls.__instance = super(Singleton,cls).__new__(cls)
        # with lock: statement is used to acquire and release a lock automatically, ensuring tht only one thread 
                    # can access a shared resource at a time, it simplifies lock management and prevents common 
                    # errors like forgetting to release a lock
        return cls.__instance

"""
As lock will slow down our process, so we need to optimize it,
    we need to understand ,when we need to execute this if condition
    with cls.__lock:
        if cls.__instance is None:  
            cls.__instance = super(Singleton,cls).__new__(cls)
    
    we have to execute this if condtion at first time only when instnace is None and create the instance
    i.e take the lock only if my __instance is None
    when instance is None, multiple thread whant to take the lock, but one will take the lock 
"""
# so optimize: so are taking lock only for the first time
import threading 

class Singleton:
    __instance = None 
    __lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: # if __instnace is None at the first time only take the Lock
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