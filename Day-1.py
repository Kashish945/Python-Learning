## topic covered - print function, data types, comments, variables, keywords, identifiers, input function, type function, type conversion, literals, operators



## Print Function
print(15)
print("kashish",15, 20, 25)
print(False)
print(True)
print("bat","ball","play","like",sep="/") 
print("kashish",end=" ")
print("pimpalshende")


## data types
# Basic types -(int, float, bool, str, complex)
# Container types - (list, tuple, set, dict)
# User-defined types - (class, object)

# integer - range 1e307
print(12)
# float - range 1e-308 to 1e308
print(1.5)
# boolean - True or False
print(True)
print(False)
# complex
print(3+4j)
# string
print("kashish")
print('kashish')
print("""kashish""")

# Container types
# list - ordered, mutable, allows duplicate elements
print([1, 2, 3, 4, 5,5])
#TUple - ordered, immutable, allows duplicate elements, use small brackets
print((1, 2, 3, 4, 5,5))
# set - unordered, mutable, does not allow duplicate elements
print({1, 2, 3, 4, 5})
# dictionary - unordered, mutable, does not allow duplicate keys, key-value pairs
print({"name":"kashish","age":20,"city":"pune"})


## comments- to enhance code redability and maintainability

# This is a single-line comment

"""
This is a multi-line comment.there is no such comment in python
"""

## variables - to store data in memory, variable name should start with a letter or underscore, can contain letters, numbers and underscores, case-sensitive
 # no variable decleration

name = "India"
print(name)
a= 10
b=20
print(a+b)

 # dynamic typing - no need to declare variable type, python automatically detects the type of variable.it is used in python,php .
 # static typing - need to declare variable type,python doest support static typing. it is used in java, c++, c#, etc
 
# varible is not binded to any type , so it can be reassigned to any type of value. it is called as dynamic binding
name = 4
print(name)
name=True
print(name)

# static binding- one variable is binded to one type of value, so it can not be reassigned to any other type of value.

# special syntax for variable assignment
a=5;b=4;c=1
print(a,b,c)
a,b,c=5,4,1
print(a,b,c)
a=b=c=32
print(a,b,c)


##keywords - reserved words in python, which can not be used as identifiers. it is case-sensitive. there are 35 keywords in python 3.10.0
import keyword
print(keyword.kwlist)

## Identifiers - names given to variables, functions, classes, modules, etc. in python. 
# it can contain letters, numbers and underscores. 
# it should start with a letter or underscore not with digit and special characters.
# it is case-sensitive.
# keywords cannot be used as identifiers
_="pune"
__=10
sum10= "intuition"
fun_function= "function"
print(_,sum10,fun_function,__,sep="\n")


## Taking input from user - 
# input() function is used to take input from user. 
# it always returns string type value. 
# we can use int(), float(), bool() to convert the input value to required type.
city=input("Enter your city name:")
print("city:",city)
marks=int(input("enter your marks:"))
print("marks:",marks)
input(prompt="what is your name:")

#code summation of two numbers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
sum=a+b
print(sum)

# type function
print(type(10))
print(type(10.5))
print(type(True))
print(type("kashish"))

## Type conversion - converting one data type to another data type 

# implict type conversion - python automatically converts one data type to another data type. it is also called as type casting.
print(10+10.5)
print(10+True)
print(10+False)
print(10+4+10j)

#explicit type conversion - we can convert one data type to another data type using built-in functions. it is also called as type casting.
# int() - converts to integer
print(int(10.5))
print(int("10"))
# float() - converts to float
print(float(10))
# str() - converts to string
print(str("abc"))

##Literals - fixed values assigned to variables
#types of literals - string, integer, float, boolean, complex, list, tuple, set, dictionary

#numeric literals - integer, float, complex
a=0b1010 #binary literal
b=0o12 #octal literal
c=0xA #hexadecimal literal
print(a,b,c)

#floating point literal
x1=10.5
x2=1.5e2
x3=1.5e-2
print(x1,x2,x3) 

#complex literal
x4=10+5j
x5=10j
print(x4,x5)
print(x4,x4.real,x4.imag)

# string literal
s1="cashish"
s2='kaashish'
s3="""kkashish"""
char='k'
multi_line="""This is a multi-line string literal
which can span multiple lines."""
raw_string=r"This is a raw string literal\n which does not escape special characters."
print(s1,s2,s3,char,multi_line,raw_string,sep="\n")

#boolean literal
b1=True+2
b2=False+10
print(b1,b2)

#special literal
a=None
print(a)
# why use none - to represent the absence of a value or a null value. it is used to initialize variables, function arguments, and return values. it is also used to represent the end of a list, tuple, or dictionary.


## Operators - special symbols used to perform operations on operands. it is used to perform arithmetic,   comparison, logical, bitwise, assignment, identity, membership operations.

# types of operators
# 1) Arithmetic operators - +, -, *, /, %, **, //
a=10
b=3
print(a+b,a-b,a*b,a/b,a%b,a**b,a//b)

# 2) Comparison operators - ==, !=, >, <, >=, <= 
print(a==b,a!=b,a>b,a<b,a>=b,a<=b)

# 3) Logical operators - and, or, not
print(a>5 and b<5,a>5 or b<5,not a>5)

# 4) Bitwise operators - &, |, ^, ~, <<, >> binary me cam atta hai. image processing me use hota hai.to convert b/w image in binary format.
print(a & b, a | b, a ^ b, ~a, a << 2, a >> 2)

# 5) Assignment operators - =, +=, -=, *=, /=, %=, **=, //=
a=b
a+=b
a-=b
a*=b
a/=b
a%=b
a**=b
a//=b
#print(a,a1,a2,a3,a4,a5,a6,a7,sep="\n")

# 6) Identity operators - is, is not. check if two variable is in same memory location or not. it is used to compare the memory location of two variables.
print(a is b, a is not b)

# 7) Membership operators - in, not in. check if one variable is present in a other varible sequence or not. it is used to check if a value is present in a list, tuple, set, or dictionary.
print(a in [10, 20, 30], a not in [10, 20, 30])
x=[10, 20, 30]
c=30
print(c in x, c not in x)