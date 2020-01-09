#--- IF STATEMENT ---#
var1 = 12
if(var1 == 12):
    print("Value is OK")
if(var1 < 20):
    print("Value is less")

#--- IF ELSE ---#
var2 = 100.001

if(var2 >= 101):
    print("Value is greater")
else:
    print("Value is lesser")

#--- IF ELSE IF ---#
var3 = 123
if(var3 <= 100):
    print("Value in range 1")
elif(var3 <= 150):
    print("Value in range 2")
elif(var3 <= 200):
    print("Value in range 3")
else:
    print("Value in range 4")

#--- NESTED IF ---#
var4 = 456
if(var4 % 2 == 0):
    print("Value is odd")
    if(var4 > 100):
        print("Value is greater than 100")
