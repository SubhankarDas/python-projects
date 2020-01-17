import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

df = pandas.read_csv("cars1.csv")
X = df[["Weight", "Volume"]]
y = df[["CO2"]]

#--- SCALING ---#
# scaling is required when it is difficult to compare values with different measurement units.
# such as comparing kilograms to liters or altitude to time.
# in cars.csv, weight 790gm and volume 1000ccm are some what comparable
# but in cars1.csv, weight 790gm and volume 1 litre (1000ccm) are not comparable
# here we need to scale the values to a comparable unit.
# scaling can be done in many ways, here we use standardization formula.


# new val. = (original val. - mean) / std. dev.
# scale weight value: (790 - 1292.23) / 238.74 = -2.1
# scale volume value: (1.0 - 1.61) / 0.38 = -1.59
# now we can compare -2.1 (weight) and -1.59 (volume)
scale = StandardScaler()
scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()  # create the regression model
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])  # scale these values

predictedCO2 = regr.predict(scaled)
print("Predicted CO2:", predictedCO2)
