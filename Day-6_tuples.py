## day-6

### Tuples :- tuples are read only datatype. useful when the data intigrity have to maintain or keep (data intigrity is important)

## CREATE
t1=()
t2=(1,2,3,4,5,8)
T3= ("hellow",11,3)

# 2d tuples
t=(1,2,4,5,(2,3))

type(t)
t6 = tuple("goa")
t3 =tuple([1,2,3,4,5])


## ACCESS
print(t2)
print(t2[-1])
print(t2[:2])
print(T3[0][0])

## EDIT :- tuples are immutable so cant edit
## ADD :- tuples are immutable so cant add

## DELETE
del t1
# del t2[-1] cannot possible

## OPERATION
t2+t3
for i in t2:
    print(i)
1 in t2
print(1 not in t2)

## FUNCTIONS 
print(len(t2))
print(max(t2))
print(min(t2))
print(sum(t2))
print(sorted(t2))
print(t2,reverse=True)



