### WORK WITH FILES 
## Reference: http://www.easypythondocs.com/fileaccess.html

## File handling:
# - r  Read only mode.The file pointer is placed at the start of the file, ready for reading. If the file does not exist, it will return an error.
# - w  Write mode. This will overwrite what is currently in a file. If the file doesn’t exist it will create a new one.
# - a  Append mode. This will append (add) to the end of an existing file and not overwrite any contents. If the file doesn’t exist it will create a new one.
# - x  Create mode. This will create a file. If the file already exists, it will return an error.


## Open a file
f = open("C:\Diego Ingegneria\Approfondimenti\Python\Video Corso Youtube\My_text_file.txt","r") # open and read a file

print(f.read()) # read file text in console
print(f.readline()) # it reads the first line then moves to se following one
print(f.readline())
print(f.readline())

f.close() # close opened file

## Edit a file

f = open("C:\Diego Ingegneria\Approfondimenti\Python\Video Corso Youtube\My_text_file.txt","a") # open and append a file

f.write("This is a text to append")
f.close()

f = open("C:\Diego Ingegneria\Approfondimenti\Python\Video Corso Youtube\My_text_file.txt","r") # open and read a file
print(f.read())
f.close()

## Create a file
f =  open("C:\Diego Ingegneria\Approfondimenti\Python\Video Corso Youtube\Test_file.txt", "x")
f.write("This file was create using Python")
f.close()

## Remove a file
import os 

os.remove("C:\Diego Ingegneria\Approfondimenti\Python\Video Corso Youtube\Test_file.txt") # remove file

# verify if a file exists
f =  open("C:\Diego Ingegneria\Approfondimenti\Python\Video Corso Youtube\Test_file.txt", "x") # create file
f.write("This file was created using Python")
f.close()

if os.path.exists("C:\Diego Ingegneria\Approfondimenti\Python\Video Corso Youtube\Test_file.txt"):
    os.remove("C:\Diego Ingegneria\Approfondimenti\Python\Video Corso Youtube\Test_file.txt") # remove file
    print("File was removed")
else:
    print("File does not exist")




## Create and remove a folder
import os 

try:
    os.mkdir("C:\Diego Ingegneria\Approfondimenti\Python\Video Corso Youtube\My_folder") # create a folder
except OSError:
    print ("Creation of the directory failed" )
else:
    print ("Successfully created the directory")

try:
    os.rmdir("C:\Diego Ingegneria\Approfondimenti\Python\Video Corso Youtube\My_folder") # remove a folder
except OSError:
    print ("Removal of the directory failed" )
else:
    print ("Successfully removed the directory")