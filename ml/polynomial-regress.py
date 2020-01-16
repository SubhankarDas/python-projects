import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# hour of the day
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14,
     15, 16, 18, 19, 21, 22]
# speed of car passing toll at the corresponding hour
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99,
     99, 100]

# create a polynomial regression model from data
model = numpy.poly1d(numpy.polyfit(x, y, 3))

# create evenly distributed x coordinates from 1 - 22 (100 coords)
line = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
# plots ideal x values with ideal y values using model
plt.plot(line, model(line))
plt.show()

# R square score is 0.94 i.e a very good relationship, hence poly. regress. can be used for prediction
r = r2_score(y, model(x))
print("R:", r)

# predict the speed of a car passing at 5PM
speed = model(17)
print(speed)
