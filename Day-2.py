### topic covered = if-else, nested if-else,identation, loops, break-continue-pass statement

## if-else statement - used in branching.  

# dommy login application
# let correct email=kashish@gmail.com password=kashish11

email=input("enter your email:")
if '@'in email:
    password=input("enter your password:")

    if email=="kashish@gmail.com" and password=="kashish11":
        print("login successful")
        
    elif email=="kashish@gmail.com" and password !="kashish11":
        print("password is incorrect")
        password=input("enter your password again:")
        if password=="kashish11":
            print("login successful")
        else:
            print("login failed")
    else:
        print("login failed")
        
## Identation - python uses indentation to define a block of code. it is used to define the scope of loops, functions, classes, etc. it is also called as whitespace. it is used to improve the readability of code. it is recommended to use 4 spaces for indentation.

## loops - used to execute a block of code multiple times. it is also called as iteration. there are two types of loops in python - for loop and while loop.

#used in :- e-commerce compaines to display products, social media companies to display posts, etc.

## while loop   
## sytanx => while condition:
##                  statement(s)

number=int(input("enter a number:"))
i=1
while i<=10:
    print(i*number)
    i+=1


## for loop
# syntax => for variable in sequence:
#                 statement(s)

# range function()- generate integers in given range.
# range(start,stop,step) - start is inclusive and stop is exclusive. step is optional. if step is not given then it is considered as 1.
print(list(range(1,11)))
print(list(range(1,11,2)))
print(list(range(10)))

#sequence - a collection of items. it can be a list, tuple, string, etc. it is used to iterate over the items in the sequence.
for i in "python":
    print(i)
for i in [1,2,3,4,5]:
    print(i)
for i in (1,2,3,4,5):
    print(i)
for i in {1,2,3,4,5}:
    print(i)
    
    
## when to use for loop => when you know how many times the loop will execute.
## when to use while loop => when you doesnt  know how many times the loop will execute.


## nested loop - loop inside the loop. ex => when you wanted to know how many transaction used did.

rows =int(input("enter the rows"))
for i in range(1, rows + 1):
    for j in range(0,i):
        print("*", end=" ")
    print(" ")
    

## break, continue and pass statement

# break - used in linear searching
for i in range (1,11):
  if i== 5:
    break
  print(i)
  
# continue - to not to display that product which is not in stock
for i in range(1,11):
  if i==5:
    continue
  print(i)
  
# pass - used in class, function
for i in range(1,11):
  pass