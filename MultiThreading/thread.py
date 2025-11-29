import threading
print("current  executig thread", threading.current_thread().name)



# the way to create thread 
"""
1: creating thread without using any class
2: creating thread by extending Thread class 
3: creating thread without extending the thread class 

"""

# 1: creating thread without using any class

from threading import *
def display():
    for i in range(1,11):
        print("child Thread")
t = Thread(target=display)
t.start()
for i in range(1,11):
    print("Main thread")


# 2: creating thread by extending Thread class

from threading import *

class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("Child thread-1")

t = MyThread()
t.start()