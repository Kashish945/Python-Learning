### OOPs

# Everything in python is object

##  Class
  # class is a blueprint
  # class has two imp thing : 
        # 1) data or property, 
        # 2) Functions or behavior
  # class name should be in PascalCase 
  # method => method is function which is written inside class

class ClassName:
        # attribute and methods
        pass
    
class Student:
        name = " kashish" 
  
## Objects
  # object is instance of class
  # when class is created no memory is allocated until an object is instantialized
  # syntax => obj_name = class_name()  
  
class Student:
    name = "kashish"
    college = "ABC college"

s1=Student()
s2=Student()
print(type(s1))
print(s1.college)
print(s2.name)

## Creating Attributes 
# there are two types of attribute


# 1) class attributes

# class atribute shared among all objects
class Student:
    college="IIT Bombay"
        
obj1 = Student()
obj2 = Student()

Student.college = "NIT Tricy"

print(obj1.college)
print(obj2.college)
  
## Instance Attribute
# unique for every object

# constructor => it is method in class which is automaticaly exicuted when object is created
 
class Demo:
    def __init__(self):
     print("Constructor called")    

# (__inti__ )it is istance attribute created using the constructor
# self  => refer to the current object
    
class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student("Kashish",22)
s2=Student("Treksha",23)

print(s1.name,s1.age)
print(s2.name,s2.age)


class Student:

    college="ABC" # Class variable
    def __init__(self,name):
        self.name=name # Instance variable

s1=Student("A")
s2=Student("B")

print(s1.college)
print(s2.college)

print(s1.name)
print(s2.name)


class Employee:

    def __init__(self,name,salary):

        self.name=name
        self.salary=salary

    def display(self):

        print("Name =",self.name)
        print("Salary =",self.salary)

s=Employee("Kashish",7000000)
s.display()

# calculate
class Calculator:
        def add(self,a,b):
                print(a+b) 

c=Calculator()
c.add(10,20)
print(id(c)) # object identity

# Modifying attribute
class Name:
     def __init__(self,name):
          self.name=name

s=Name("kashish")
s1=Name("nacy")
print(s.name)
s.name="treksha"
print(s.name)
del s.name # deleting attribute
del s1 # deleting object 

# Object Reference
class StudentMarks:
        def __init__(self,m1,m2,m3):
            self.m1=m1
            self.m2=m2
            self.m3=m3
        
        def total(self):
                return self.m1+self.m2+self.m3
            
        def average(self):
                return self.total()/3
            
s=StudentMarks(50,50,50)
s1=s # object reference
print(s1.total())
print(s1.average())


# Circle example
import math 
class Circle:
        def __init__(self,radius):
                self.radius= radius
        
        def area(self):
            self.calarea = math.pi*self.radius*self.radius
            return self.calarea
        
        def perimeter(self):
             return 2*math.pi*self.radius

c=Circle(7)
print(c.area())
print(c.perimeter())
            
        
