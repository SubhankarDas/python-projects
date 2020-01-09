#--- LISTS ---#
list = ["abc", 123, 45.6, "pqr", "xyz"]

print(list[3])  # item at index
print(list[2:4])  # subset of items from 3rd item to 4th item
print(list[2:])  # subset from 3rd item to last item
print(list * 2)  # prints list 2 times
print(list + ["123", 456])  # concats list with another list

#--- TUPLES --#
tup = ("abc", 123, 45.6, "pqr", "xyz")  # tuples are read only lists

print(tup[3])  # item at index
print(tup[2:4])  # subset of items from 3rd item to 4th item
print(tup[2:])  # subset from 3rd item to last item
print(tup * 2)  # prints tuple 2 times
print(tup + ("123", 456))  # concats tuple with another tuple

list[2] = 12  # valid syntax
# tup[2] = 12  # invalid syntax

#--- DICTIONARY --#
dict1 = {}
dict2 = {123: "John Doe", "role": "designer"}  # init a dictionary

print(dict1)
print(dict2)

dict1['John'] = "45,000"  # add key value pair to dictionary
print(dict1)

print(dict1["John"])
print(dict2[123])
print(dict2.get("role"))

print(dict1.keys())  # get keys of a dict
print(dict2.values())  # get values of a dict
