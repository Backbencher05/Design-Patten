# __new__() method 
            # will trigger before __init__, 
            # as write now it's None at very
            # first call of __new__, it will create the object and assign it to the __instance variable
            #  and return the instance

"""
Q:2 - why __instace is private
    we kept it private because let instance2 created and it done again __instance=None
    new object will create again
    as private is assessbale within the class only
"""

class Singleton:
    __instance = None #private: initially when we create class we don't have any object of this class
    def __new__(cls, *args, **kwargs): # we are over_riding __new__() method, as this __new__() already present in parent class i.e "object" class
        if cls.__instance is None: # i.e no object , means we have to create object
            cls.__instance = super(Singleton,cls).__new__(cls) # we are calling parent class method and over riding it so we are using super keyword (__new__() method present parent class i.e in object class)
        return cls.__instance
"""
what this line is doing ?

cls.__instance = super(Singleton,cls).__new__(cls)

- super(Singleton,cls).__new__(cls) 
         it will call actual/default implimentation of __new__() method present in object class(parent class)
    - generally when we call super method we pass "instance", but as __new__() is a class method,
        so here we are calling class method , we don't have any instance that's why we are passing "class" i.e
        i.e Singleton to super method by specifying with (,) that it is a class and call __new__() method of parent class (.__new__(cls)) , this is singleton class    

looks like,
when we call super method normally we do and caliing __init__() method
    - super().__init__()
here also we are doing same thing and calling __new__() method
    - super(Singleton, cls).__new__(cls) #as __new__ is a class method
"""

"""
Q:2 - why __instace is private
    we kept it private because let instance2 created and it done again __instance=None
    new object will create again
    as private is assessbale within the class only
"""

if __name__ == "__main__":

    instance = Singleton() # __new__() method will trigger before __init__, as write now it's None, 
                            # at very first call of __new__, it will create the object and assign it to the __instance variable
                            #  and return the instance
    print(instance)   # we got the object in "instance" variable now if someone again create the object i.e instance2 = Singleton()
                      # it again call __new__() method before __init__() and it check now our condition become false
                      # is now __instance is not None object aready created so out condition become false so it diractly return 
                      # - for instance2, No new object created in memory but for the end userit is like creating the new object but we created
                      # only one object
    instance2 = Singleton()
    print(instance2)
    # output for instnace and instanc2 
    # <__main__.Singleton object at 0x0000015A291ED580>
    # <__main__.Singleton object at 0x0000015A291ED580>
    print(instance is instance2) # True

# But This is code is Not Thread safe , as if multiple thread try to create at the same time
#     let,
#         s1 = Singleton()   
#         s2 = Singleton()
# it will create the issue