### Polymorphism

# Polymorphism is an Object-Oriented Programming (OOP) concept that allows one interface (method/function/operator) to have multiple forms or behaviors.

# Types of Polymorphism in Python
  # 1. Compile-Time Polymorphism (Method Overloading)
  # 2. Run-Time Polymorphism (Method Overriding)


## Method Overriding
# Method overriding occurs when a child class provides its own implementation of a method already defined in the parent class.

# Example 1:
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Example 2:polymorphism using a common interface
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

class Cow:
    def speak(self):
        print("Moo")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()


## Method Overloading  

# Method Overloading is the ability to define multiple methods with the same name but different parameter lists within the same class.

# Technical method overloading not work in python

# Following are the alternate way to achieve method overloading behavior

# Example 1: using default argument
class Geometry:
  def area(self,a,b=0):
    if b==0:
      print("circle",3.14*a*a)
    else:
      print("rect",a*b)
          
obj= Geometry()
obj.area(4)
obj.area(4,5)

# Example 2: Using Variable-Length Arguments (*args)
class Calculator:

    def add(self, *numbers):
        print(sum(numbers))

obj = Calculator()

obj.add(10,20)
obj.add(10,20,30)
obj.add(10,20,30,40)

# Example 3: Using keyword Argument(**kwargs)
class Student:

    def details(self, **data):
        print(data)

s = Student()

s.details(name="Kashish")
s.details(name="Kashish", age=22)

        
## Operator Overloading

# Operator Overloading is a feature in Python that allows operators to behave differently depending on the operands (objects or data types).

# It lets you define how operators such as +, -, *, ==, etc., work with objects of your own classes.

# Example 1: 
print(10 + 20)
print("Hello " + "World")
print([1,2] + [3,4])

# Example: Overloading the + Operator
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(80)
s2 = Student(90)
print(s1 + s2)

# Example: Overloading the == Operator
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student(80)
s2 = Student(80)
print(s1 == s2)

# Example: Overloading the > Operator
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

s1 = Student(90)
s2 = Student(75)
print(s1 > s2)