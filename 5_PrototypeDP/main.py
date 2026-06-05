from Zombie import Zombie
import time

if __name__ == '__main__':
    # let i want Zombie Monster
    z = Zombie(100) # we are passing health

    # let i want to create 100 Zombies
    arr = []
    for i in range(100):
        arr.append(z.clone())


    # print("these are", arr) # you can see 100 diff. object created i.e every object have diff. reference id

    # let i have changed the health of 1st object , it will not affect other objects (zombies) as for every zombie refrence if diff
    # that's why we have used deep copy
    arr[0].health = 90
    print(arr[0].health)
    print(arr[1].health) 
    print(arr[2].health) 
    arr[2].attack()
