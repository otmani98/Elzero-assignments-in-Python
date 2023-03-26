#76-78

#assign01
import random

def random_even() :

    x = random.choice(range(2,11))

    if x % 2 == 0 :

        return x
    
    else :

        return random_even()

def random_odd() :

    x = random.choice(range(1,10))

    if x % 2 != 0 :

        return x
    
    else :

        return random_odd()
    

print(f"Random Number Between 10 And 50 => {random.choice(range(10,51))}")
print(f"Random Even Number Between 2 And 10 => {random_even()}")
print(f"Random Odd Number Between 1 And 9 => {random_odd()}")



# assign 02+03+04 All of them in python folder (modules lessons)