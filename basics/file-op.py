#--- FILE HANDLING ---#

# 1. READ
# opens file in rt (read, text) mode (non writable)
f1 = open("file1.txt")  # f = open("file1.txt", "rt")
print(f1.readline())
content = str(f1.read())
print(content)


# f1.write("New text.") # io.UnsupportedOperation: not writable


# 2. WRITE
# opens file in wt (write, text) mode (non readable)
f2 = open("file1.txt", "wt")
f2.write("Old text file contents are over written here. ")

# print(f2.read()) # io.UnsupportedOperation: not readable
f2 = open("file1.txt")
print(f2.read())


# 3. APPEND
# opens file in at (append, text) mode (not readable)
f3 = open("file1.txt", "at")
f3.write("Adding some more lines of text. \nThis is a new line with a line break")

# print(f3.read())  # io.UnsupportedOperation: not readable


# 4. CREATE
# creates a non existing file in appending mode (non readable) and raise FileExistsError if file exists
f4 = open("file2.txt", "x")

f4.write("Writing some content.\n")
f4.write("Writing new content.")
# print(f4.read())  # io.UnsupportedOperation: not readable

# IMPORTANT - CLOSE ALL OPENED FILES
f1.close()
f2.close()
f3.close()
f4.close()
