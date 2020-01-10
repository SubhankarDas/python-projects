#--- USER INPUT ---#
name = input("Enter your name: ")
print(name)

marks = 84
str = "Your name is {} and got {}"  # string format

print(str.format(name, marks))

str = "Name: {nme}    Marks: {mrks}"  # string format with params
print(str.format(nme=name, mrks=marks))
