### topic covered - build-in functions, built-in modules


## build in functions

print("kashish")
name = input("enter name:")
print(type(name))

#abs() = printing absoulate value
print(abs(-4))

#pow() = power 
print(pow(2,4)) 

# min and max
print(min(1,2,3,5))   
print(max(1,2,3,5)) 
print(min("kashish")) 
print(max("kashish")) 

# round =used in decimal value printing
c= 22/7
print(round(c))

# divmod = it returns the tuples
print(divmod(5,2))

# bin/oct/hex = give binary, octal,hexdecimal value
print(bin(4))
print(oct(4))
print(hex(4))

# id = find address in memory
a = 13
print(id(a))

# ord =  return unicode code 
print(ord("A"))

# len
print(len("kashish"))

# sum()= dive sum of list tuple etc
print(sum({1,2,3,4}))

# help() = give documentation of any other function etc
#print(help('print'))



## Built-in Module

# modules = cosider a module to be the same as a code library. 
# a file containing a set of functions you want to include in your application.
# ex= math, random, os, time
 
#print(help('modules'))

# math module
import math 
print(math.factorial(4))
print(math.pi)
print(math.e)
print(math.ceil(2.34))
print(math.floor(2.34))

# Random
import random
print(random.randint(1,100))
a = [1,2,3,5,4]
print(random.shuffle(a))

# time
import time
print(time.time())
print(time.ctime())
print("hello")
time.sleep(1)
print("world")

# os
import os
print(os.getcwd())
print(os.listdir())