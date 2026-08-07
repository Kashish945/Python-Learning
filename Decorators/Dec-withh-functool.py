## Decorators with functools.wraps

# functools.wraps is a decorator for decorators. It preserves the original function's metadata (such as its name, docstring, annotations, and module) when you wrap it with another function.
# Without @wraps, the decorated function appears to be the wrapper function instead of the original function.
# wraps(func) copies the original function's metadata to the wrapper.
#t preserves attributes like __name__, __doc__, __module__, __annotations__, and __wrapped__.


from functools import wraps

def decorator(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
      print("befor")
      return func(*args, **kwargs)
  return wrapper
    
@decorator
def greet():
  """Greet the User"""
  print("Hello")
  
print(greet.__name__)
print(greet.__doc__)

# __name__ returns the name of the function.
#__doc__ returns the documentation string (docstring) of the function.



## Common Built in Decorators

## 1. @staticmethod
# Used when a method doesn't need access to the instance (self) or the class (cls).
# Example :
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3,4))


## 2. @classmethod
#Receives the class (cls) as the first argument instead of an instance.
# Example: 
class Student:
    school = "ABC"
    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()


## 3. @property
# Allows youu to access a method like a attribute
# Example:
class Circle:
  def __init__(self,r):
    self.r = r
    
  @property
  def area(self):
    return 3.14*self.r*self.r
  
c = Circle(5)
print(c.area)  # area is accessed without parentheses. 
    