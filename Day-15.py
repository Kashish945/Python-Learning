### Relationship 

# there are three type of relationship
  # 1) Aggregation ( Weak has-a )
  # 2) Composition ( strong has-a )
  # 2) Inheritance ( is-a )
  
## 1) Aggregation

# Aggregation is a relationship where one class has another class as a member, but both objects can exist independently.

# The child object can exist without the parent.
# it is a weak relationship.
 
# Example 1
class Engine:
    def start(self):
        print("Start Engine")
        
class Car:
    def __init__(self,engine):
        self.engine = engine # aggregation

    def drive(self):
        self.engine.start()
        print("Car is moving")
        
# Engine Object Exists independently
engine= Engine()

# Car uses the existing engine object
car = Car(engine)

car.drive()


# Example 2 :- Customer has a address
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        
    def edit_profiles(self, new_name, new_city,new_pin,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pin,new_state)
        
class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
        
    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pin=new_pin
        self.state=new_state
        
add= Address("kolkata",700156,"WB")
cust= Customer("kashish","male",add)

cust.edit_profiles("sanju","gurgoan",120112,"haryana")

print(cust.address.city)
print(cust.address.pincode)

print(cust.address.pin)
print(cust.address.state)


## Composition

# Composition is a relationship where one class owns another class. If the parent object is destroyed, the child object is also destroyed.

# The child object cannot exist independently.
# It is a strong relationship.

# Example 1 
class Engine:
    def start(Self):
        print("Engine Started")
        
class Car:
    def __init__(self):
        self.engine=Engine()  # composition
        
    def drive(self):
        self.engine.start()
        print("Car is moving")
        
car = Car()
car.drive()        
# Explaination : The Engine object is created inside the Car. If the Car object is deleted, its Engine object is also gone. Therefore, this is Composition.