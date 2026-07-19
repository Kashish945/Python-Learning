## Day - 7

### Dictionary :- key-value pairs

## RULES :-
# 1) Dictionary has no indexing
# 2) it is mutable types
# 3) key -> immutable, value ->they can be mutable
# 4) Keys should be unique

## CREATE
d={} # empty dictionary
d1={"name":"Nitish","age":"22"}
print(d1)

d2={(1,2,3):"Nitish"}
print(d2)

# 2D dictionary
d3={"name":"kashish","college":"GCOEC","marks":{"Math":80,"science":90,"eng":87}}
print(d3)

## ACCESS ;- data can be fetch through the key
print(d3["name"])
print(d3["marks"])
print(d3['marks']['eng'])

## EDIT
d['name']='kashish'
print(d)
d3['marks']['histroy']=98
print(d3)

## ADD
d['age']=22
print(d)
d3['marks']['math2']=98
print(d3)

## DELETE
del d2

# delete induvidual key value pair
del d1['age']
print(d1)

d1.clear

## OPERATION :- + , * not possible 
# only print the key
for i in d3:
    print(i)
    
# print key-value pair
for i in d3:
    print(i,d3[i])
 
#check if it exist in key   
print("kashish" in d3)  # print false
print("name" in d3)  # print true
    
    
## FUNCTION :-
print(len(d3))
print(max(d3))
print(min(d3))
print(sorted(d3))
print(sorted(d3,reverse=1))

# function specific to dictionary
print(d3.keys())
print(d3.values())

