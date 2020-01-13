import numpy

# data set
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39,
        80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# percentile - gives us the max. value under which a given percentage of values lie
# ex: what is the age under which 90% of the ages lie
percentile = numpy.percentile(ages, 90)

print("Percentile : ", "90% of the ages lie below age", percentile)
