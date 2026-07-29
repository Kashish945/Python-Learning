### Inheritance

# Inheritance is an OOP (Object-Oriented Programming) concept in which one class (child/subclass) acquires the properties and methods of another class (parent/superclass).
# It allows code reusability and helps create a hierarchy of classes.
# Inheritance represents an "Is-A" relationship.
# Private methods are not inherited
# Example:   Dog is an Animal, Car is a Vehicle.


# NEED OF INHERITANCE :
  # Promotes code reuse.
  # Reduces code duplication.
  # Makes programs easier to maintain.
  # Supports method overriding and polymorphism.
  # Models real-world relationships effectively.
  
# Example 1:  
class User:
    def login(self):
        print("login")
    
    def register(self):
        print("Register")
        
class Student(User):
    def enroll(self):
        print("Enroll")
        
    def review(self):
        print("review")
        
stu1= Student()

stu1.enroll()
stu1.login()
stu1.register()
stu1.review()

        
# Example 2: inheriting constructor
class Phone:
     def __init__(self, price,brand,camera):
        print("inside phone class constructor")  
        self.price=price
        self.brand=brand
        self.camera=camera
        
class Smartphone(Phone):
    pass
  
s1=Smartphone(20000,"realme",13)      
# Explanation :- 1st check inside smartphone class if contructor not found then goes to phone class and call phone class constructor


# Example 3: Inheriting private member
class Phone:
     def __init__(self, price,brand,camera):  
        self.price=price
        self.__brand=brand
        self.camera=camera
        
class Smartphone(Phone):
    pass
  
s1=Smartphone(20000,"realme",13)
# print(s1.__brand) it will crash here
# Explanation : child class cannot inherited the private members of parent class

# Example 4 : Method Overriding -> Polymorphism
class Phone:
     def __init__(self, price,brand,camera):
        print("inside phone class constructor")  
        self.price=price
        self.brand=brand
        self.camera=camera
        
     def buy(self):
        print("Buying the Phone")   
        
class Smartphone(Phone):
    def buy(self):
        print("Buying the SmartPhone")   
    
s1=Smartphone(20000,"realme",13)
s1.buy()
# Explanation : in method overriding  if same methods/function are their in both child and parent class then the prefernce is always given to child class method .


# Example 5: class Parent (Problem-1)
class Parent:
    def __init__(self,num):
        self.__num=num
        
    def getnum(self):
        return self.__num

class Child(Parent):
    def show(self):
        print("Inside child class")    
        
son=Child(100)
print(son.getnum())
son.show()
# O/p :-  100 , Inside child class


# Exampke 6 : Problem-2 (two constructor)
class Parent:
    def __init__(self,num):
        self.__num=num
        
    def getnum(self):
        return self.__num

class Child(Parent):
    def __init__(self,val,num):
        self.__val=val
    def getval(self):
        return self.__val 
        
son=Child(100,10)
# print("Parent num:",son.getnum()) this will throw error, solution --> Example 10
print("child val:", son.getval())
# Explanation : child constructor get invoked First, but the parent constructor is not trigger/call/invoked hence the method is not invoked.


# Example 7: Problem-3
class A:
    def __init__(self):
        self.val1=100
    def display1(self,val1):
        print("class A:",self.val1)
        
class B(A):
    def display2(self,val1):
        print("class B:",self.val1)
        
obj=B()
obj.display1(200)
# Explanation : it will print 100 because the self.val1 is called.


## Super () function

# Example 8: Super()
# super --> can access parent method and cannot access attribute. super cannot be called outside the class.
class Phone:
     def __init__(self, price,brand,camera):
        print("inside phone class constructor")  
        self.price=price
        self.brand=brand
        self.camera=camera
        
     def buy(self):
        print("Buying the Phone") 
        
     def return_phone(self):
        print("REturning a phone")

class Featurephone:
    pass
        
class Smartphone(Phone):
    def buy(self):
        print("Buying the SmartPhone")   
        super().buy()
    
s1=Smartphone(20000,"realme",13)
#s1.super().buy() this cannot work
s1.buy()
# Expanation : super keyword call/invoke the constructor of the parent class.


# Example 9 : calling constructor using super keyword 
# super should be a first statement inside child constructor otherwise it will not work. 
class Phone:
     def __init__(self, price,brand,camera):
        print("inside Phone constructor")  
        self.price=price
        self.brand=brand
        self.camera=camera
        
class Smartphone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price,brand,camera) # 1st statement always
        self.os=os
        self.ram=ram
        print("inside Smartphone constructor")
        
s = Smartphone(20000,"samsung",12,"Android",2)
print(s.os)
print(s.brand)


# Example 10:  Solution of example no.6
class Parent:
    def __init__(self,num):
        self.__num=num
        
    def getnum(self):
        return self.__num

class Child(Parent):
    def __init__(self,val,num):
        super().__init__(num)
        self.__val=val
    def getval(self):
        return self.__val 
        
son=Child(100,10)
print("Parent num:",son.getnum()) 
print("child val:", son.getval())


# Example 11 : Problem of super
class Parent:
    def __init__(self):
        self.num=100
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.val=200
        
    def show(self):
        print(self.num)
        print(self.val)
        
obj=Child()
obj.show()
# Expanation : parent class attribute will be called .      


# Example 11 : Problem of super
class Parent:
    def __init__(self):
        self.num=100   
    def show(self):
        print("parent:",self.num)
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.val=200
        
    def show(self):
        
        print("child:",self.val)
 
dad=Parent()
dad.show()   # this will call parent method     
son=Child()
son.show()  # this will call child method(method overrriding)