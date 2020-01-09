#--- FUNCTIONS ---#
def add(a, b):                                                       # function defination
    "This function adds two number and returns the result."          # function docs
    # function body
    print("Adding", a, "and", b)
    # return statement
    return a+b


print("Result: ", add(1, 2))

#--- PASS BY REFERENCE - BY DEFAULT IN PYTHON ---#


def passByRef(var):
    var[1] = 10
    print("Inside func():", var)


var = [1, 2, 3]
passByRef(var)
print("Outside func():", var)

#--- PASS BY VALUE ---#


def passByVal(var):
    var = [1]
    print("Inside func():", var)


var = [1, 2, 3]
passByVal(var)
print("Outside func():", var)

#--- PARAMETERS ---#


def display(val1, val2=2):          # parameters: val1, val2 (default = 2)
    print(val1, "---", val2)


display(1, 2)                       # uses default order of params
display(val2=200, val1=100)         # uses param names
display(1)                          # optional val2 uses default


def func(param1, *params):          # undefined no. of params tuple using *
    print(param1, params)


func(12, 34, 56)
func("a", "b", "c")
