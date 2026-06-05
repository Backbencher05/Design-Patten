# # Super method

# """
# super() is a built-in method which is useful to call the super class constructor, variable and method fro  the child class

# """

# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def display(self):
#         print('Name:', self.name)
#         print('age', self.age)



# class Student(Person):
#     def __init__(self, name, age, rollno, marks):
#         super().__init__(name, age)
#         self.rollno = rollno
#         self.marks = marks


#     def display(self):
#         super().display()
#         print('Roll No:,', self.rollno)
#         print('Marks', self.marks)

# s1 = Student('Aditya', 22, 101, 90)
# # s1.display()



# class P:
#     a = 10
#     def __init__(self):
#         self.b = 20

#     def m1(self):
#         print('Parent Instance method')

#     @classmethod
#     def m2(cls):
#         print('Parent Class method')

#     @staticmethod
#     def m3():
#         print('PArent Static method')


# class C(P):
#     a = 888
#     def __init__(self):
#         self.b = 999
#         # super().__init__()
#         print(super().a)
#         print(self.b)
#         super().m1()
#         super().m2()
#         super().m3()

# # c = C()



# Various Important Points about super():

"""
Case-1: From child class we are not allowed to access parent class instance variables by using
super(),Compulsory we should use self only.
But we can access parent class static variables by using super().
"""

class P1:
    a = 10
    def __init__(self):
        self.b=20

class C1(P1):
    def m1(self):
        print(C1.a)
        print(super().a)
        print(self.b)

c = C1()
c.m1()

"""
Case-3: From child class class method , we cannot access parent class instance methods and 
constructors by using super() directly(but indirectly possible). But we can access parent class static 
 class methods. 

"""
class P:   
    def __init__(self):   
        print('Parent Constructor')   
    def m1(self):   
        print('Parent instance method')   
    @classmethod   
    def m2(cls):   
        print('Parent class method')   
    @staticmethod   
    def m3():   
         print('Parent static method')   
    
class C(P):   
     @classmethod   
     def m1(cls):   
        #  super().__init__()#--->invalid   
         #super().m1()--->invalid   
         super().m2()   
         super().m3()   
    
C.m1()   

"""
Output: 
Parent class method 
Parent static method 

 
 Important ***********

From Class Method of Child class,how to call parent class instance 
methods and constructors

class A:   
    def __init__(self):   
        print('Parent constructor')   
       
    def m1(self):   
        print('Parent instance method')   
   
class B(A):   
    @classmethod   
     def m2(cls):   
         super(B,cls).__init__(cls)   
         super(B,cls).m1(cls)   


B.m2()   

Output: 
Parent constructor 
Parent instance method 
 
Case-4: In child class static method we are not allowed to use super() generally (But in special way 
we can use) 
1) class P:   
2)     def __init__(self):   
3)         print('Parent Constructor')   
4)     def m1(self):   
5)         print('Parent instance method')   
6)     @classmethod   
7)     def m2(cls):   
8)         print('Parent class method')   
9)     @staticmethod   
10)     def m3():   
11)         print('Parent static method')   
12)    
13) class C(P):   
14)     @staticmethod   
15)     def m1():   
16)         super().m1()-->invalid   
17)         super().m2()--->invalid   
18)         super().m3()--->invalid   
19)    
20) C.m1()   
RuntimeError: super(): no arguments 
 
How to call parent class static method from child class static method by using super(): 
1) class A:   
2)           
3)     @staticmethod   
4)     def m1():   
5)         print('Parent static method')   
6)    
7) class B(A):   
8)     @staticmethod   
9)     def m2():   
10)         super(B,B).m1()   
11)    
12) B.m2()   
Output: Parent static method 

"""



"""
From Class Method of Child class,how to call parent class instance
methods and constructors:
1) class A:
2)
def __init__(self):
3)
print('Parent constructor')
4)
5)
def m1(self):
6)
print('Parent instance method')
7)
8) class B(A):
9)
@classmethod
10) def m2(cls):
11)
super(B,cls).__init__(cls)
12)
super(B,cls).m1(cls)
nd
# 202, 2 Floor, HUDA Maitrivanam, Ameerpet, Hyderabad - 500038,
25 DURGASOFT,
 040 – 64 51 27 86, 80 96 96 96 96, 92 46 21 21 43 | www.durgasoft.com13)
14) B.m2()
Output:
Parent constructor
Parent instance method
Case-4: In child class static method we are not allowed to use super() generally (But in special way
we can use)
1) class P:
2)
def __init__(self):
3)
print('Parent Constructor')
4)
def m1(self):
5)
print('Parent instance method')
6)
@classmethod
7)
def m2(cls):
8)
print('Parent class method')
9)
@staticmethod
10) def m3():
11)
print('Parent static method')
12)
13) class C(P):
14) @staticmethod
15) def m1():
16)
super().m1()-->invalid
17)
super().m2()--->invalid
18)
super().m3()--->invalid
19)
20) C.m1()
RuntimeError: super(): no arguments
How to call parent class static method from child class static method by using super():
1) class A:
2)
3)
@staticmethod
4)
def m1():
5)
print('Parent static method')
6)
7) class B(A):
8)
@staticmethod
9)
def m2():
10)
super(B,B).m1()
11)
12) B.m2()
Output: Parent static method

"""