
## Iteration
# iteration is a general term for taking each item of someting.one after another. any time you a loop.explicit or implicit to go over agroup of items that is iteration.

# Example
num=[1,2,3,4,5]
for i in num:
    print(i)


## Iterator
# An Iterator is an object that allow the proggrammer to traverse through a sequence of data without having to store the entier data in the memory.

# Example
L=[x for x in range(1,10000)]
#for i in L:
#    print(i*2)

import sys
print(sys.getsizeof(L)/64)

# another way to do same example 
x=range(1,100000)
print(sys.getsizeof(x)/64)

# explanation: the first example creates a list of 10000 numbers and stores it in memory, while the second example creates a range object that generates numbers on-the-fly without storing them all in memory. This is more memory efficient.


## Iterable
# iterable is an object, which one can iterate over.
# it generates an iterator when passed to the iter() method.

# Example
l=[1,2,3,4,5]
print(type(l)) # <class 'list'>
# l is an iterable
print(type(iter(l))) # <class 'list_iterator'>

# Point to remember :
  # 1. Every iterator is also an iterable
  # 2. Not every iterable is an iterator
  
# Trick to check iterable and iterator
    # 1. every iterable has an iter function
    # 2. every iterator has both the iter function and next function

a=2
print(dir(a))

t=(1,2,3,4,5)
print(dir(t))

s={1,2,3,4,5}
print(dir(s))
# if dir contain iter then it is iterable
# if dir contain both iter and next then it is iterator

l=[1,2,3,4,5]
iter_l=iter(l)
print(dir(iter_l))


## Understanding how for loop work 
no=[1,2,3,4,5]
for i in no:    
    print(i)
    
# Explantion: 1)fetch the iterator using iter() function
#             2) call next() function to get the next  item from the iterator

## making our own for loop 

def my_for_loop(iterable):
    iterator=iter(iterable)
    while True:
        try:
           print(next(iterator)) 
        except StopIteration:
            break

a=[1,2,3,4,5]
b=range(1,11)
c=(1,2,3,4,5)
d={1,2,3,4,5}
e={0:1,1:2}

my_for_loop(a)
my_for_loop(b)
my_for_loop(c)
my_for_loop(d)
my_for_loop(e)


## Confusing point:
num=[1,2,3,4,5]
iter_obj1=iter(num)
iter_obj2=iter(iter_obj1) # <list_iterator object at 0x000001F3D8A1B4C0>
id(iter_obj1) # 2234567890128
id(iter_obj2) # 2234567890128

# Both iterators point to the same object in memory because when iter_obj1 is passed to iter_obj2 , the iter obj_2 is itself a iterator and it returns itself when passed to iter() function. So both iterators point to the same object in memory.


## Benefits of using iterators:
# 1. Memory efficient: Iterators do not store the entire data in memory, they generate the data on-the-fly, which makes them more memory efficient.
# 2. Lazy evaluation: Iterators generate the data only when it is requested, which allows for lazy evaluation and can improve performance in certain situations.


## Lets Create our own range function
class MyRange:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
        
    def __iter__(self):
        return Myrange_iterator(self)
    
    
class Myrange_iterator:
    def __init__(self,iterable_obj):
        self.iterable=iterable_obj
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start>=self.iterable.stop:
            raise StopIteration
        current=self.iterable.start
        self.iterable.start+=1
        return current
 
x=MyRange(1,11)   
print(type(x)) # <class '__main__.MyRange'>
for i in x:
    print(i)    