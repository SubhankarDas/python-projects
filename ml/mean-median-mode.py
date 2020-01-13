import numpy
from scipy import stats

# data set
ages = [12, 32, 13, 12, 16, 24, 25, 13, 12, 14]


# mean - average value of the data set i.e (val1 + val2 + ... + valn)/n
mean = numpy.mean(ages)

# median - middle most value of the set, if there are two values then (val1 + val2)/2
median = numpy.median(ages)

# mode - most occuring element in the data set
mode = stats.mode(ages)

print("Mean   : ", mean)
print("Median : ", median)
print("Mode   : ", mode.mode[0])
