## Generator

# python generator is a simple way to create iterators.

# Why use generator?
    # 1. It is easy to implement
    # 2. It is memory efficient because it yields one item at a time instead of storing all the items in memory.
    # 3. It is faster than using a list because it does not require the overhead of creating and storing a list in memory.
    # 4. It can be used to create infinite sequences, which is not possible with lists.
    # 5. It can be used to create pipelines of data processing, where each stage of the pipeline can yield data to the next stage without having to store all the data in memory.


# generator function dont have return statement, instead they have yield statement. when a generator function is called, it returns a generator object without even beginning execution of the function. when the next() method is called for the first time, the function starts executing until it reaches yield statement, which returns the yielded value. The next time next() is called, the function continues executing from where it left off (it remembers all the data values and which statement was last executed). This allows it to produce a series of values over time, instead of computing them all at once and sending them back like a list.

# EXAMPLE 1 
def gen_demo():
    yield 1
    yield 2
    yield 3
    
gen=gen_demo()
print(gen) 
#print(next(gen)) # 1
#print(next(gen)) # 2
#print(next(gen)) # 3    

for i in gen:
    print(i) 
    

# EXAMPLE 2
def square(num):
    for i in range(1,num+1):
        yield i*i
        
gen_obj=square(5)
for i in gen_obj:
    print(i)
  
    
# EXAMPLE 3 : Range of numbers using generator
def My_range(start,end):
    for i in range(start,end):
        yield i
        
gen=My_range(20,30)
for i in gen:
    print(i)
    
    
## Generator Expression
# generator expression is a compact generator notation in python. it is similar to list comprehension but instead of creating a list and storing all the values in memory, it creates a generator object that generates values on-the-fly.

gen_exp = (i**2 for i in range(1,101))
for i in gen_exp:
    print(i)