# R-squared: relationship between the x and y values of data set.
# if there is no relationship then linear regression can't be used to predict future values.
# the value of r-squared (r) lies between 0 and 1.
# 0 = no relationship      1 = 100% relationship
# r denotes how well the data fits in linear regression.

from scipy import stats
import matplotlib.pyplot as plt

# ages of car in years
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# speeds of the respective cars in kmph
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# calculate the stats
slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + intercept  # get speed from age i.e linear


speed = myfunc(10)  # predicted speed of a 10 year old car

# r = -0.75 (there is a relation but not perfect, so lin. reg. can be used)
print("R:", r)
print("Predicted speed:", speed)


model = list(map(myfunc, x))

# in the plot diagram mostly data points are near to the
# line corresponding to model hence data is a good fit.
plt.scatter(x, y)
plt.plot(x, model)
plt.show()
