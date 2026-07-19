## FUNCTIONS :- block of code 

# benefits of function :- code Modularity, code Reusability, code Readability


# 1) Abstraction
# 2) Decomposition
# 3) component of function => def, valid identifier, bracket, argument, : ,string
# 4) by default the function return none

def is_even(i):
  """
    Optional docstring which tells us about the function, that what input are required , what will the function return
  """
  x=i%2==0
  return x 

for i in range(1,11):
  print(is_even(i))
  
print(is_even.__doc__)


# 5) Parameters VS Argument
# Parameters =>

# Argument

# i) Default argument
def power(a=1,b=1):
    print(a**b)
power(2,3)
power(2)
power(1)

# ii) Positional argument

# iii) Keyword argument => useful in large parameter
power(b=2,a=3) # it overide the parameter
 
# iv) Arbitrary argument
def flexi(*number):
    product=1
    print(type(number))
    for i in number:
        product=product*i
    print(product)
    
flexi(1)
flexi(1,2)
flexi(1,2,3)
flexi(1,2,3,4)


## GLOBAL VARIABLE Vs LOCAL VARIABLE

    
def f(y):
    x=1 # local variable
    x+=1
    print(x)
    
x=5  # global variable
f(x) 
print(x) 
# o/p=> 2 5

def g(y):
    print(x) # if local varible is not define then global variable value is used. 
    print(x+1) # it will create a new varibale . it will not change the gloable variable

x=5
g(x)
print(x)
# o/p => 5 6 5 

def h(y):
    # x+=1 # leads to error because this line try to change the value of global variable anf it is not allowed 
    global x
    x+=1  #  using this we can change the value of global varibale but this method is not recommended
x =5
h(x)
print(x)

def f(x):
    x =x+1
    print("in f(x): x = ",x)
    return x
x=3 
z=f(x)
print("in main program scope: z = ",z)
print("in main program scope: x = ",x)
# o/p => 4 4 3


## Nested Function => function inside function

def f():
    print("inside f")
    def g():
        print("inside g")
    g()
f()
# we cannot call inner function directly because the inner function is hidden to main program . if you directly call the inner function it will throw error
# note :- dont call outer func inside inner fun and inner function inside outer function at a time it will end up in infinte loop

def g(x):
    def h():
      x = "abc"
    x=x+1
    print("inside g(x): x = ",x)
    h()
    return x
x=3
x=g(x)


def g(x):
    def h(x):
      x = x+1
      print("inside h(x): x = ",x)
    x=x+1
    print("inside g(x): x = ",x)
    h(x)
    return x
  
x = 3
z = g(x)
print("in main program scope: z = ",z)
print("in main program scope: x = ",x)
# o/p => 4 5 4 3


## EVERYTHING IN PYTHON IS AN OBJECT , function too
# behaviour of function is just like data type

# function as object
def f(num):
    y = num**2 
    print(y)
    return y
f(2)
x = f
print(type(x))
x(2)
del f
# f(2) throw error. we can delete function . reference of f get delete but reference of x will stay. 
x(4)
l=[1,2,3,4,x]
print(l)
l= [1,2,3,4,x(5)]
print(l)


def func_a():
    print("inside function a")

def func_c(z):
    print("inside function c")
    return z()
 
print(func_c(func_a))

#o/p => inside function c , inside function a, none 


def f():
    def x(a,b):
        return a+b
    return x
val= f()(3,4)
print(val)