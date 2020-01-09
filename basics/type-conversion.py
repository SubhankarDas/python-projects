#--- DATA TYPE CONVERSION ---#
var1 = int(12.34)  # float to int
var2 = int("1234")  # string to int

var3 = float(12)  # int to float
var4 = float("12.34")  # string to float

print(var1)
print(var2)
print(var3)
print(var4)

var5 = complex(12, 23)  # creates a complex number
print(var5)

var6 = str(123)  # converts to string
print(var6 + '456')

var7 = list((12, 34))  # converts to list
print(var7)

var8 = tuple([12, 34])  # converts to tuple
print(var8)
