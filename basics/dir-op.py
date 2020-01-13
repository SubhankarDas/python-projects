import os

#--- FILE DELETION AND EXISTS CHECK ---#
print(os.path.exists("file2.txt"))  # False

f = open("file2.txt", "at")  # creates the file
f.close()

print(os.path.exists("file2.txt"))  # True

# delete file if exists
if(os.path.exists("file2.txt")):
    os.remove("file2.txt")  # deletes the file


#--- DIRECTORY OPERATIONS ---#
os.mkdir("test-dir")  # creates a directory
os.rmdir("test-dir")  # removes a directory
