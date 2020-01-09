#--- VARIABLES AND DATA TYPES ---#
var1 = 10  # integer
var2 = 12.34  # float
var3 = "John Doe"  # string
var4 = True  # boolean

print(var1)
print(var2)
print(var3)
print(var4)

del var1  # deletes reference to var1

#--- STRING ---#
str = var3  # string initialization

print(str[1])  # character at index
print(str[1:6])  # substring from 2nd char to 6th char
print(str[2:])  # substring from 3rd char to last char
print(str * 3)  # prints str 3 times
print("Mr. " + str)  # concat string
