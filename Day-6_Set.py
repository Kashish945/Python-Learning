## DAY-6

### SET

# Four Rule :- 
# 1. set donot allow duplicate
# 2. sets have no indexing/slicing
# 3. sets dont allow mutable data types
# 4. sets itself is a mutable data type

## CREATE
S1= set() # empty set
s2={1,2,4,5,6}
s3={1,2,3.4,"hellow"}
s4={1,2,1,2,2,3,4,4,5,5,}
print(s4)

# s={[1,2,3],"hellow "} with list it is not possible
s={(1,2,3),"hello"} # with tuples it is possible because tuples is mutable 
print(s) # sets have no indexing .it uses hashing

# s5={{1},{2}} 2d,3d,4d sets are not possible


## ACCESS :- not possible
# s2[0] indexing not suppoted

## EDIT :- not possible

## ADD 
print(id(s2))
s2.add(7)
print(s2)
print(id(s2))

## DELETE
# del :- cannot delete with indexing
del S1

# pop :- delete the last element but using hashing
s2.pop()
print(s2)

# remove
s2.remove(7)
print(s2)

## OPERATOION
s1={1,2,3,4,5}
s2={3,4,5,6,7}
# s1+s2, s1*3 is not possible
for i in s1:
    print(i)
1 in s1

## FUNCTION

print(len(s1))
print(max(s1))
print(min(s2))
print(sum(s1))
print(sorted(s1))
print(sorted(s1,reverse=True))

# function that are specific to set
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))

