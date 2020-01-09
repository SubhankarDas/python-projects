#--- WHILE LOOP ---#
var1 = 1
while(var1 <= 3):
    print("Loop No.:", var1)
    var1 += 1

print("While ends here")

#--- FOR LOOP ---#
ran = range(1, 4)  # range from 1 to 3
for var2 in ran:
    print("Loop No.: ", var2)

print("For ends here")

names = ["John", "Dany", "Bob"]  # loop over a list
for name in names:
    print("Hello " + name)
print("End of names")

str = "Hello World!"
for char in str:
    print("*" + char + "*")

#--- NESTED LOOPS ---#
str = ''
for i in range(5):
    for j in range(i):
        str += " * "

    print(str)
    str = ''
