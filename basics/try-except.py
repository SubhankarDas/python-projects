#--- HANDLE EXCEPTION ---#
try:
    print(x)
except:
    print("Error occured!")  # catch exception
else:
    print("No error occured!")  # no exception occured
finally:
    print("Error handled!")  # try except finished


#--- RAISE EXCEPTION ---#
try:
    raise Exception("Error message!")
except Exception as ex:
    print(ex)


#--- CUSTOM EXCEPTION ---#
class MyException(Exception):  # override exception class for custom exception
    def __init__(self, msg):
        super().__init__(msg)


try:
    raise MyException("Custom message!")
except MyException as ex:
    print("Msg:", ex)
