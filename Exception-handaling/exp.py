## Exception handling

# Exception handling in Python is the process of detecting and managing runtime errors so that your program can continue running or fail gracefully instead of crashing.

## Need of Exception Handaling
    # 1. Prevents program crashes.
    # 2. Improves program reliability.
    # 3. Allows graceful error recovery.
    # 4. Separates normal logic from error-handling code.
    # 5.Makes debugging and maintenance easier.

# Example 1:
try:
  x=10/0
  
except ZeroDivisionError:
  print("You cannot divide by Zero")
  
finally:
  print("Execution completed.")
  
  
# Example 2: multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)

except ValueError:
    print("Invalid input. Please enter an integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

finally:
    print("Program ended.")