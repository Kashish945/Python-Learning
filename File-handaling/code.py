## File Handling

# File handling means creating, opening, reading, writing, updating, and deleting files using Python.

# Example 1: Opening file and reading a file
file = open("data.txt","r")
data=file.read() # reading a file
print(data)
file.close() # closing a file

# Example 2:
file=open("data.txt","r")
print(file.read(4)) # read the first 4 character
print(file.readline()) # read one line

# Example 3: Writing the file
file=open("data.txt","w")
file.write("I am a python developer")
file.close
# Note : "w" deletes the existing content and writes new content.

# Example 4: Appending to File
file=open("data.txt","a")
file.write("\n Welcome to My github")
file.close()

# Example 5: Using with -- Recommended way
with open("data.txt","r") as file:
  data=file.read()
  print(data)
# Python automatically closes the file after leaving the with block.


# Example 6: Writing Multiple lines

# Way 1:
with open("student.txt","w") as file:
  file.write("kashish\n")
  file.write("Sayali\n")
  file.write("Preksha\n")
  
# Way 2:
students=["Ron\n", "jonh\n", "Ritchie\n"]
with open("student.txt","w") as file:
  file.writelines(students)
  
  
# Example 7: File pointer
# python maintain a file pointer that tells you the current position in the file

# 1 : tell()
with open("data.txt","r")as file:
    print(file.tell()) # tell() Returns the current position.
    print(file.read(5))
    print(file.tell())
    
# 2 : seek() moves the file pointer 
with open("data.txt", "r") as file:
    print(file.read(5))
    file.seek(0)  # moves the pointer back to beginning
    print(file.read(5))
 
    
# Example 8 : Handaling file exception
try:
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File not found")
    
    
# Example 9: Creating a file 
file = open("newfile.txt", "x") # if file already exist then python raises FileExistsError
file.close()

# Example 10 :checking if the file exist
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")
    
# Example 11: Deleting a file
os.remove("data.txt")