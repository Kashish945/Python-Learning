## String

# strings are sequence of characters. in python specifically, strings are sequence of unicode characters.

# operation on string =>

## 1.creating string
c = "kashish didn't come!!"
print(c)
k = 'hello'
print(k)
t = '''used when we have to write multiline string. used in bloging website'''
print(t)
a = str("hello") #type coversion string


## 2. Accessing substring fron the string

# concept of indexing
c="India"
print(c[3]) # positive indexing (goes left to write)
print(c[-1]) # negative indexing
# types of indexing => positive , negative (right to left)

# concept of slicing => multiple char are extracted
a = "hello world"
print(a[0:5]) # 1st no included last no.not included 
print(a[2:]) # from 2 to end 
print(a[:4])  # from starting to 4
print(a[:]) #print entire string
print(a[2:6:2]) # last tell step so 1 char skip ho jayega
print(a[0:6:-1]) # steps cannot be negative, hence it print empty
print(a[-5:-1:2])
print(a[::-1]) # reverse string
print(a[-1:-5:-1]) # reverse print hoga


## 3. Editing and Deleting the string

c = "hello"
print(c)
# strings are InMutable(can't change) data types
# can reasign a string 
c = "world"
print(c)
# cannot add new characters

# deletion
del c
#print(c)
c = "hello"
# del c[0] this cannot be done 
# del c [:3:2]  this also cannot be done
  
# summary => string cannot be edited . we cannot delete string partially complete deletion is done only

## 4. String Operation
 
# arithematic operation => +, * only possible
print("hello"+"world") # concat
print("*"*14)
print("kashish"*4)

# Relation operator
print("hi"=="hello")
print("hi"!="hello")
print("mumbai">"pune") # lexiographically => alphabetical order follows 
print("goa"<"kolkata")
print("hi"<"Hi") # small letter came first hence it is bigger.

# logical operation
print("hello" and "world")
# empty string = false
# non-empty string = true
print(""and"hello")
print(" "or"wolrd")
print("hello"or"world")
print(not"hello")
print(not"")

# loops operation
c = "kashish"
for i in c:
    print(i)
for i in c[1:4]:
    print(i)
for i in c[1:6:2]:
    print(i)
for i in c[::-1]:
    print(i)
    
# membership operation

print("k"in c)
print("hi"not in c)
print("H" in c) # false=> capital H is not present, small h is there


## functions in string
 
# comman function => len, max,min, sorted
a = "kolkata"
print(len(a)) # print length of string
print(max(a)) # print max charater according to ascii value
print(min(a)) # print min charater according to ascii value
print(sorted(a)) # print sorted string in ascending order in form of list
print(sorted(a,reverse=True)) # print sorted string in descending oder in the form of list

# capitalize, title, upper, lower, swapcase
print(a.capitalize()) # capitalize only first word
print(a.title()) # capitalize all first letter of each word
print(a.upper()) #uppercase
print(a.lower()) #lowercase
print(a.swapcase()) # convert lower to upper/upper to lower

# count =>count the substring
print("it is raining".count("i"))

# find/index
print("it is raining".find("i")) # if char occurrance is frequent then it return  1 st postion
print("it is raining".find("rain"))
print("kashish".find("t"))
print("kashish".index("i"))
#print("kashish".index("t")) #throw error

#summary => if char/string is not present in given string . then in find it return -1 and in index it throw and error(substring not found)

# endswith/ startswith
print("it is raining".endswith("ing"))
print("it is raining".startswith("it"))  

# format =>used in login page . after login to show hello_name of user( hello kashish!!)
print("hi mt name is {} and I am {}".format("kashish", 22))
print("hi mt name is {1} and I am {0}".format("kashish", 22)) # in formating position is fixed
print("hi mt name is {name} and I am {age}".format(name="kashish",age=22))
print("hi mt name is {name} and I am {age}".format(name="kashish", age=22, weight=50))

# isalnum/isalpha/isdecimal/isdigit/isidentifier
print("kaj2".isalnum())
print("kal3@".isalnum())
print("flat".isalpha())
print("flat20".isalpha())
print("20A".isdigit())
print("20".isdigit())
print("hello world".isidentifier())
print("hello_world".isidentifier())
print("heloo".isascii())

# split function => most useful
print("i am kashish".split())
print("i am kashish".split("am"))

# join =>reverse of split
c = ['what', 'is','python','?']
print(" ".join(c))
print("-".join(c))

# REplace
print("hi i am kashish".replace("kashish","kashu")) # replace(start, end)

# strip => strip remove trailing and leading spaces
name = "         kashish               "
print(name)
print(name.strip())