### OPPs Basic

## Reference Variable
# A reference variable is a variable that refers to (points to) an object in memory.

class Student:
    def __init__(self,name):
        self.name=name

std=Student("kashish")
s2= std
print(id(std))
print(id(s2))
del std
print(s2) # obj is not deleted because s2 still refers to it


## Pass by Object Reference

# Pass by Object Reference means that the function receives a reference to the same object passed by the caller. If the object is mutable, changes to the object are visible outside the function. If the parameter is reassigned to a new object, only the local reference changes.

class Customer:
    def __init__(self,name):
        self.name=name
 
def greet(customer): 
    print(id(customer)) # same id 2371007837056
    customer.name="sanju"
    print(customer.name)
    print(id(customer)) # same id 2371007837056
            
custobj =Customer("kashish")
print(id(custobj)) # same id 2371007837056
greet(custobj)
# if you pass a object to function and function change the valuse then it will affect outside the function also.
# class objects are also mutable like lists, dict and sets

print(custobj.name)


class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
 
def greet(customer):
    if customer.gender=='Male':
        print("hello",customer.name,"sir")
    else:
        print("hello",customer.name,"ma'am")
    
    cust2=Customer("Sanju","Male")
    return cust2   
            
cust =Customer("kashish","Female")
new_cust=greet(cust)
print(new_cust.name)


## Collection of Object
#A collection of objects means storing multiple objects of the same class (or different classes) inside a Python collection such as: List, Tuple, Set ,Dictionary
#This allows us to process many objects together.

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age= age
    def intro(self):
        print("I am",self.name,"and i am",self.age,"year old")
        
s1=Student("kashish",22)
s2=Student("sonali",22)
s3=Student("treksha",23)

l=[s1,s2,s3]

for i in l:
    print(i.name,i.age)
    i.intro()
    
# Creating object directly in list
class Student:
    def __init__(self, name):
        self.name = name

students = [
    Student("A"),
    Student("B"),
    Student("C")
]

for student in students:
    print(student.name)    
  
  
    
## Static
#A static variable (class variable) is a variable that is declared inside the class but outside any methods. It has only one copy, which is shared among all instances (objects) of the class.
# Static varible are created outside the constructor whereas the instance variable are created inside the constructor
class Student:
    college = "ABC College"    # Static (Class) Variable
    def __init__(self, name):
        self.name = name        # Instance Variable

s1 = Student("Kashish")
s2 = Student("Janhavi")

print(s1.college)
print(s2.college)

# Changing Static Variable using class name
class Student:
    college = "ABC College"

s1 = Student()
s2 = Student()

Student.college = "XYZ College"

print(s1.college)
print(s2.college)
print(Student.college)