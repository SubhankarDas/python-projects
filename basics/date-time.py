import datetime

datetime1 = datetime.datetime.now()  # current date time
print(datetime1)

datetime1 = datetime.datetime(1993, 3, 18)  # create date time from values
print(datetime1)

print(datetime1.strftime("%x ---> %B"))  # formatted string from date time

print(datetime.datetime.now() - datetime1)  # calculate time difference
