"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt
from prompt_toolkit.key_binding.bindings.named_commands import end_kbd_macro


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    a = 1
    b=2


# ex2
def exercise2():
    pass


# ex3
def exercise3():
    pass


# ex4
def exercise4():
    pass


# ex5
def exercise5():
    pass


# ex6
def exercise6():
    counter=0
    trial=input("enter a string")
    for word in trial.split():
        if word=="emma":
            counter+=1
    print(counter)



# ex7
def exercise7():
    list1=[1,2,3,4,5,55,66,65,23,45,23]
    list2=[65,87,24,5,7,2234,2345,2347,78654,99]
    list3=[]
    for i in list1:
        if i%2 !=0:
            list3.append(i)
    for i in list2:
        if i%2 ==0:
            list3.append(i)
    print(list3)
    pass


# ex8
def exercise8():
    pass


# ex9
def exercise9():
    pass


# ex10
def exercise10():
    pass


# ex11
def exercise11():
    pass


# ex12
def exercise12():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 1")
    #exercise6()
    exercise7()
