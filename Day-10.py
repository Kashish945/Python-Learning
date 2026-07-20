## Recursion Function => function calling itself.

# using loop
def multiply(a,b):
    result=0
    for i in  range(b):
         result= result+a
    print(result)

multiply(3,4)

# using recursion
def mul(a,b):
    if b==1:
        return a
    else:
      return a+mul(a,b-1)

print(mul(3,4))

# factorial of n number
def fact(num):
      if num<=1:
         return 1
      else:
          return num*fact(num-1) 
        
print(fact(5)) 

# check string is palindrome or not
def pali(s):
    if len(s)<=1:
        print("palindrome")
    else:
        if s[0]==s[-1]:
            pali(s[1:-1])
        else:
          print("not a palindrome")
pali("madam")
pali("malayalam")
pali("abba")
pali("kashish")


# The Rabbits Problem :- Fibonacci pattern

#pair of rabbits produces another pair every month starting from the second month. How many rabbit pairs are there after n months?
#The number of rabbit pairs follows the Fibonacci sequence:
#Month 1 → 1 pair
#Month 2 → 1 pair
#Month 3 → 2 pairs
#Month 4 → 3 pairs
#Month 5 → 5 pairs
#Month 6 → 8 pairs

def fib(m):
    if m==0 or m==1:
        return 1
    else:
        return fib(m-1)+fib(m-2)
print(fib(12))
# this code is highly inefficient . tc=2^n

#memoization =>dynamic programming 
def memo(m,d):
    if m in d:
      return d[m]
    else:
      d[m]=memo(m-1,d)+memo(m-2,d)
      return d[m]
  
d={0:1,1:1}
print(memo(48,d))
# this is efficient code 

# power set .eg list=[1,2], then power set = [[],[1],[2],[1,2]]
def power_set(nums):
    result = []
    def solve(index, subset):
        # Base case
        if index == len(nums):
            result.append(subset[:])   # Store a copy
            return

        # Include current element
        subset.append(nums[index])
        solve(index + 1, subset)

        # Backtrack
        subset.pop()

        # Exclude current element
        solve(index + 1, subset)

    solve(0, [])
    return result


nums = [1, 2]
print(power_set(nums))

