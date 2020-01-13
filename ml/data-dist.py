import numpy
import matplotlib.pyplot as plot

#--- UNIFORM DATA DISTRIBUTION ---#
# generate a huge random uniform data set to work with
data = numpy.random.uniform(0, 5, 250)

# disply a histogram from data set
plot.hist(data, 5)  # HISTOGRAM 1
plot.show()

plot.hist(data, 10)  # HISTOGRAM 2
plot.show()


# HISTOGRAM 1: Displays histogram with 5 bars (0-1,1-2, 2-3, 3-4, 4-5) for dist. of 0-5
# HISTOGRAM 2: Displays histogram with 10 bars (0-0.5-1,1-1.5-2, 2-2.5-3, 3-3.5-4, 4-4.5-5) for dist. of 0-5

#--- NORMAL DATA DISTRIBUTION ---#
# generate a normal data set or Gaussian data distribution
# normal data set is where all the values are close to a mean value
# here the mean is 5 and std. is 1.
data = numpy.random.normal(5.0, 1.0, 100000)

plot.hist(data, 100)  # HISTOGRAM 2
plot.show()

# HISTOGRAM 3: Normal distribution graph i.e bell shaped curve
