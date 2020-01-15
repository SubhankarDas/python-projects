from scipy import stats
import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# calculate key values from (x,y)
(slope, intercept, r, p, std_err) = stats.linregress(x, y)


# function to get position of y corresponding to x (y = mx + c)
def func(x):
    return slope * x + intercept


# map func(x) into a list i.e list of y values
model = list(map(func, x))

plt.scatter(x, y)  # plot scatter diagram
plt.plot(x, model)  # plot linear regression with set of (x,y)
plt.show()
