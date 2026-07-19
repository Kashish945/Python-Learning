## topic covered :- MUtability, Garbage Collection, Variable Referencing

### VARIABLE AND REFERENCE MEMORY

# in ram in register the variable are store
# memory is represent in hexadecimal form 
# python calls variable as name

a=4
print(id(a))
print(hex(a))

# call by object Reference

## Aliasing 
a = 5
b = a # aliasing
print(id(b))
print(id(a))
del a # we delete the references
print(b)
print(id(b))

## Referene counting
import sys
a="kashish"
b=a
c=b
print(sys.getrefcount(a))

x= "iampink"
y=x
w=y
print(sys.getrefcount(x)) # it print count as variable+1



## Garbage Collection
# occupid and unused memory 


# wierd behaviour of pyrhon
# 1. WB
a=2
b=a
c=b
print(sys.getrefcount(a)) 
# explanation :- the ans idealy should be 4. but it showing large no because 2 is very common no. hence . 2 is already created the program just referencing to it . More common a no more large will its count . uncommon no have small count.

# 2. WB
# -5 to 256 id of two varible (a=2,b=2) storing same no. will be same but when the number goes behond the limit the id changes. it is the software optimization technique to make program fast.

# 3. WB
a="kashish"
b="kashish"
print(id(a))
print(id(b)) # id will be same for both a and b

a="kashish inst tech"
b="kashish inst tech"
print(id(a))
print(id(b))
# explaination :- if you have valid identifier then the id will be same . but if  there is no valid identifier then the momory location varies and hence the id varies. so example one has same id but example two have different id.


### MUTABILITY

# Mutability refers to ability to change or edit the data in it's memory location
# Mutability depends on data type
# Immutable data types => Int, Float, String, Boolean, Tuples, Complex
# Mutable data types => List, Dictionary, Sets

# in Immutable data type the id change as the data type is added 
a="hello"
print(id(a))
a=a+"world"
print(id(a))
 
# in Mutable data type the id remain same
a=[1,2,3]
print(id(a))
a.append(5)
print(id(a))

# if you are working with mutable data type then for copying variable clonnong is used.
# cloning => cpoying the item in different address loaction
l1=[1,2,3,5]
print(id(l1))
l=l1[:] # cloning
print(id(l))
 
# list inside tuples :- so the list is mutable we can make  changes in it without changing its address
a=(1,2,3,[4,5])
a[-1][-1]=500
print(a)

# tuple inside list :- tuples is immutable data type so change or editing cannot be done without changing its address.
a = [1,2,3,(4,5)]
# a[-1][-1]=500 this will thow error
print(a)

a=[1,2]
print(id(a))
b=[3,4]
print(id(b))
c=(a,b)
print(id(c))
c[0][0]=100
print(c)
print(id(c))

# over list when concation done the address get change hence concatation  not down 