## Decorators

# Definition : A decorator is a special function in Python that modifies or extends the behavior of another function (or class) without changing its original source code.

# decorators works because python treats functions as first-class objects.

# basic syntax of decorator:
def decorator(function):
    def wrapper():
      print("before function")
      function()
      print("after function")
    return wrapper
      

# Need Of Decorators:
    # 1. Code Reusability: Decorators allow you to reuse code across multiple functions or methods, reducing redundancy and promoting cleaner code.
    # 2. Separation of Concerns: Decorators help separate the core logic of a function from additional functionality, making the code more modular and easier to maintain.
    # 3. Avoid duplicate code
    # 4. Follow the DRY (Don't Repeat Yourself) principle
    # 5. Add functionality without modifying existing functions
    # 6. Improve code readability
    # 7. Separate business logic from utility code
 
    
# Example 1:
def logger(func):
    def wrapper(a,b):
      print("function started")
      result=func(a,b) 
      print("function ended")
      return result
    return wrapper
  
@logger
def add(a, b):
    return a + b
  
@ logger
def sub(a, b):
    return a - b 
  
print(add(2,2))
print(sub(2,2))
#logger code is written once

# Example 2: Decorators with arguments
def decorator(func):
    def wrapper(a, b):
        result = func(a,b)
        return result
    return wrapper
  
@decorator
def multipy(a, b):
  return a * b

print(multipy(1,3))
 

# Example 3:Using *args and **kwargs
def loggr(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is called with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper
  
def add(a, b):
    return a + b

# Applying the decorator
add = loggr(add)  

add(3, 5) # Output: Function add is called with arguments: (3, 5) and keyword arguments: {}

## *args and **kwargs allow a function to accept a variable number of arguments. They are especially useful in decorators because the decorator usually doesn't know what parameters the wrapped function will have.

# *args collects all positional arguments into a tuple.
# **kwargs collects all keyword arguments into a dictionary.


# Example 4: Measuring execution time
import time
def timer(func):
   def wrapper(*args, **kwargs):
     start=time.time()
     result=func(*args,**kwargs)
     end =time.time()
     print("Execution time: ", end-start)
     return result
   return wrapper
 
@timer 
def work():
  time.sleep(2)
  print("working....")
  
work()


# Example 5: Authentication Decorator
logged_in=True
def login_required(func):
  def wrapper():
    if logged_in:
      func()
    else:
      print("please login")
  return wrapper
  
@ login_required
def profile():
  print("welcome user")

profile()  


# Example 6: Multiple Decorators
def decor1(func):
  def wrapper():
    print("decorator 1 before")
    func()
    print("decorator 1 after")
  return wrapper

def decor2(func):
  def wrapper():
    print("Decorator 2 before")
    func()
    print("Decorator 2 after")
  return wrapper

@decor1
@decor2
def hello():
  print("hello")

hello()

# Explanation
'''hello()
   ↓
decor1
   ↓
decor2
   ↓
Original Function
'''
