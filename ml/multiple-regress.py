import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")  # read data file

X = df[["Weight", "Volume"]]  # independent variables
y = df[["CO2"]]  # dependent variables

regr = linear_model.LinearRegression()  # create linear model
regr.fit(X, y)

# predict CO2 emission of car with weight is 2300g and volume is 1300ccm
predictedCO2 = regr.predict([[2300, 1300]])
print("Predicted CO2:", predictedCO2)

# coefficient is the degree of relationship with the unknown variable
# y = 2x (unknown var. = 2 x known var.) here coefficient = 2
coef = regr.coef_
print(coef)

# Coef. of weight = 0.00755095 (with increase in 1 gm of weight, CO2 emission increases by 0.00755095 gm.)
# Coef. of volume = 0.00780526 (with increase in 1 ccm of volume, CO2 emission increases by 0.00780526 gm.)

# predictedCO2 = previous predictedCO2 + (increased weight)
predictedCO2 = regr.predict([[3300, 1300]])
print("Predicted CO2:", predictedCO2)

# prev. prediction + (coeff. x increased weight) + (coeff. x increased volume)
res = 107.2087328 + (1000 * 0.00755095) + (0 * 0.00780526)
print("Result CO2:", res)
