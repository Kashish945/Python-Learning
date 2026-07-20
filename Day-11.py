## Lambda Function =>
 
# A lambda function is a small anonymous (unnamed) function that can have any number of arguments but only one expression.
# used in single line
# sytax => lambda arguments:experssion

x=lambda x:x**2
print(x(9))

a=lambda x,y:x+y
print(a(2,3))


## Difference between lambda and Normal Function
# 1) Lambda function has no return value
# 2) can be written in one line
# 3) Not used for code reusability
# 4) No name 

## Why Lambda 
# used along with higher order function(it is function that require another function for input or function returing another function)

# checking first letter is a or not 
b=lambda x:x[0]=='a'
print(b('apple'))
print(b("banana"))

# check even or odd
b=lambda x:'Even'if x%2==0 else 'Odd'
print(b(2))
print(b(3))

# Higher Order Function
def return_sum(func,L):
    result=0
    for i in L:
        if func(i):
            result = result+i
    return result
  
L=[11,14,21,23,56,18,45,29,28]

x= lambda x:x%2==0
y= lambda x:x%2!=0
z= lambda x:x%3==0

print(return_sum(x,L))
print(return_sum(y,L))
print(return_sum(z,L))

## Map Function

# The map() function applies a given function to every element of an iterable (such as a list, tuple, or set) and returns a map object (an iterator).
# syntax => map(function, iterable)

# map apply logic to each item of list
l=[1,2,3,4,5,6,7]

# multiple each item of list with 2
x=map(lambda x:x*2,l)
print(list(x))

# check even,odd number in list
print(list(map(lambda x:x%2==0,l)))

# Retriving From Data
student=[
  {
    'name':"Rick Smart",
    'collge': "MIT",
    'age':20
  },{
    'name':"Richard William",
    'collge': "Oxford",
    'age':21
  },{
    'name':"John Smith",
    'collge': "NTU",
    'age':22
  }
]
x=map(lambda student:student['name'],student)
y=map(lambda student:student['age']>=21,student)
print(list(y))
print(list(x))

## Filter Function

# The filter() function is used to select elements from an iterable based on a condition.
# work on condition
# syntax => filter(function,iterable)
# function -> return true and false
# iterator -> list, tuples, set, etc.

l=[1,2,3,4,5,6,7]
print(list(filter(lambda x:x>4,l)))

Fruits=["apple","orange","mango","guava"]
c=list(filter(lambda Fruits:'e' in Fruits,Fruits))
print(c)

## Reduce Function

# The reduce() function applies a function cumulatively to the elements of an iterable and returns a single value.
# It is available in the functools module.
# syntax => reduce(function, iterator)

import functools

l=[1,2,3,4,5,6,7]

y=functools.reduce(lambda x,y:x+y,l)
print(y)

x=functools.reduce(lambda x,y:x if x>y else y,l) # retriver max 
print(x)

z=functools.reduce(lambda x,y:x if x<y else y,l) # retrive min 
print(z)


## List Comprehension

# technique using which you can create a list from another list
# syntax => new_list = [expression for item in iterable]

l=[1,2,3,4,5,6,7]
l1=[item*2 for item in l]
print(l1)
l2=[item**2 for item in l]
print(l2)
l3=[i**2 for i in range(10) if i%2!=0]
print(l3)

## Dictionary Comprehension

# Dictionary comprehension is a concise way to create dictionaries.
# Syntax => new_dict = {key: value for item in iterable}

d={"name":"kashish","gender":"female","age":22}
print(d.items())
d1={key:value for key,value in d.items() if len(key)>3}
print(d1)
# o/p =>{'name': 'kashish', 'gender': 'female'}

d2={item:item**2 for item in l}
print(d2)
# o/p => {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

d3={item:item**2 for item in l if item%2==0}
print(d3)
# o/p => {2: 4, 4: 16, 6: 36}