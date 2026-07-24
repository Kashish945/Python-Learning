### OOPs :- Encapsulation

## Encapsulation
    # It is the process of binding data (variables) and methods (functions) together into a single unit (class) and restricting direct access to some of the object's data.

# Need for Encapsulation
    # Protects data from unauthorized access.
    # Prevents accidental modification of data.
    # Improves security.
    # Makes code modular and maintainable.
    # Hides internal implementation from users.

    
##   Access Specifiers in Python

# 1) Public Members
    # Public members can be accessed from anywhere.
class Animal:
        def __init__(self):
                self.aniname = "Panda"

a= Animal()
print(a.aniname)


# 2) Protected Members (_)
    # Protected members are intended for use within the class and its subclasses.
    # Python does not enforce this restriction—it is only a convention.
    
class Animal:
        def __init__(self):
                self._aniname = "Panda"

a= Animal()
print(a._aniname)  
# Even though _aniname is accessible, programmers should treat it as an internal attribute.
 
  
# 3)Private Members (__)
    # Private members are name-mangled by Python to reduce accidental access.
    
class Animal:
        def __init__(self):
                self.__aniname = "Panda"

a= Animal()
# print(a.__aniname) throw an AttributeError 
print(a._Animal__aniname) # Accessing private variable


class Student:
    def __init__(self):
        self.__marks = 95

s = Student()
print(s.__dict__)


# Private Methods
class Student:
    def __show(self):
        print("Private Method")
    def display(self):
        self.__show()

s = Student()
s.display()


# Getter and setter
    # A common way to achieve encapsulation is by providing controlled access to private data.

class BankAccount:
         def __init__(self,balance):
                self.__balance= balance
         def get_balance(self):
                return self.__balance
         def set_balance(self,amount):
                if amount>=0:
                    self.__balance = amount
                else:
                    print("Invalid Balance")

account= BankAccount(50000)
print(account.get_balance())
account.set_balance(80000)
print(account.get_balance())

# Using @property
    # Python provides a cleaner way to implement getters and setters.

class Student:
        def __init__(self,marks):
                self.__marks=marks
                
        @property
        def marks(self):
                return self.__marks
        
        @marks.setter
        def marks(self,value):
                if value >=0:
                    self.__marks = value
                    
s= Student(90)
print(s.marks)
s.marks=99
print(s.marks)

  
# Note :- nothing in python are Truly Private, members can be modified from outside the class 

class Demo:

    def __init__(self):
        self.__x = 10

d = Demo()

d.__x = 20

print(d.__dict__) # o/p =>{'_Demo__x': 10, '__x': 20}
# explanation : Notice what happened:  _Demo__x → Original private attribute, __x → A new instance attribute you created. Python didn't modify the original attribute.

# to change the original one
d._Demo__x = 30
print(d._Demo__x)


## Why Use __ then?
    # If it isn't truly private, why use it?
    # There are two main reasons:
        # 1) Prevent accidental access or modification.
        # 2) Avoid name conflicts in inheritance.

#Example:
class Parent:
    def __init__(self):
        self.__x = 10

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__x = 20

c = Child()

print(c.__dict__)
