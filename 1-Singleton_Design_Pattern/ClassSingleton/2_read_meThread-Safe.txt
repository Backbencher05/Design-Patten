We’ll take this in two steps:

1️⃣ First, I will show you how the simple Singleton breaks under multithreading.
2️⃣ Then, we will build the correct thread-safe Singleton.

Let’s go step by step.

⭐ Step 1: The simple Singleton we wrote (NO thread-safety)

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

--> This works perfectly in single-threaded code.
But in multithreading, two threads can run at the same time.


⭐ Step 2: Understand how two threads break Singleton

Imagine two threads running together:

Thread T1:

- Enters __new__()
- Checks: _instance is None → True
- Gets ready to create instance…

Thread T2:

- Also enters __new__()
- Checks: _instance is None → True
 (T1 hasn’t finished yet)
- Gets ready to create instance…

Now both threads create separate objects.

So you end up with:

Instance A (created by T1)
Instance B (created by T2)

❌ This violates Singleton.

⭐ Step 3: Let me simulate this for you

(Don’t worry — just read the explanation. The code is for demonstration.)

🔥 Multithreading breaking Singleton:


import threading

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

def create_instance():
    obj = Singleton()
    print(id(obj))

threads = []

for _ in range(5):
    t = threading.Thread(target=create_instance)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

🔍 Expected output (multiple different IDs):
139948928150704
139948928150800
139948928150704
139948928150800
139948928150912

Different memory addresses = different objects created.

That means the Singleton is broken.

⭐ Step 4: Why does this happen?

Because the operation:

if _instance is None:
    create instance

is not atomic.
Between checking and assigning, another thread can slip in.
This is known as a race condition.

⭐ Step 5: How do we fix it?

We use a Lock → only one thread can enter the critical region:

if _instance is None:
    # lock here
    create instance

Lock ensures:

- Only one thread creates the object
- Other threads wait
- They see instance already exists
- They return the same instance


⭐ Step 6: Thread-safe Singleton (Final Version)

from threading import Lock

class Singleton:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock
                cls._instance = super().__new__(cls)
        return cls._instance

This is called Double-Checked Locking.

This is the version used in real systems.