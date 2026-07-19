## day-5

## list
## List vs Array
# 1 array is homogeneous wheras list is hetrogeneous
# 2.array store lineary whaeras the list does not store lineary
# 3. array are faster list is slow
# 4. list is programmer friendly

## Create
l=[]  # empty list 
l=[1,2,3,4] # homogeneous list
l=["hellow",2,3.4,'k',True,2+1j]  # heterogeneous list

# multi-dim list
# 2D
l1=[1,2,3,[4,5]]
print(l1)
# 3D
l2=[[[1,2],[3,4],[6,5]]]
print(l2)

#type conversion list
l3=list("kashish")
print(l3)

## Access
l=[1,2,3,4]
print(l[0])
print(l[-1])
print(l[1:3])
print(l[::-1])
l1=[1,2,3,[4,5]]
print(l1[-1][0])
print(l1[-1][-1])
a =[[[1,2],[3,4],[6,5],[7,8]]]
print(a[0][1][1])
# no of dimension= no of brackets

## Edit
# list in python are mutable
l=[1,2,3,4]
l[0] = 100
l[-1] = 900
print(l)
l[1:3] = [400,500,600]
print(l)

# Add
# append => add in last
l.append(1000)
l.append([5,6])
print(l)
# extend => add multiple in last
l.extend([5000,6000,7000])
l.extend("goa")
print(l)
# insert => it add in  index position
l.insert(1,"kashish")
print(l)

## delete
# del
del l2
del l1[2]
print(l1)
# remove =>index position is not known then used
l.remove("kashish")
print(l)
# pop => pop last item
l.pop()
print(l)
# clear =>not delete but empty the list
l1.clear()
print(l1)


## operator
l1=[1,2,3,4]
l2=[5,6,7,8]
print(l1+l2)
print(l1*3)
for i in l1:
    print(i)
print(4 in l1)
l3=[1,2,3,[4,5]]
print(4 in l3)

## function in list
len(l1)
min(l1)
max(l1)
sorted(l1) #sorted is not permant operation in will create a duplict
sorted(l1, reverse=True)
l1.sort() # sort is the permant operation 
l1.index(3)


# problem :- write a code which can convert first letter of each word in capital withou usint title()
sample= "how are you"
l=[]
print(sample.split())
for i in sample.split():
    print(i.capitalize())
    l.append(i.capitalize())
print(l)
print(" ".join(l))


# problem => remove all the item befor @ from email
sample = "kashish@gmail.com"
print(sample[:sample.find("@")])
 
# remove duplicates from list
l1=[1,1,2,2,3,3,4,4]
l2=[1,2,3,1]
l=[]
for i in l1:
    if i not in l:
      l.append(i)
print(l)