'''
ALGORITHM 1: LINEAR REGRESSION (MULTIPLE)

This is a regression algorithm that is used to predict values based on independent parameters and relationship 
between the independent values (X) and dependent values (y) which has to be linear in nature.
That is Y = m * X + c defines the relationship in the dataset.
Types of linear regression: 1. Simple linear regress (one independent value, one dependent value)
                            2. Multiple linear regress (multiple independent value, one dependent value)
                                    y = (m1 * x1) + (m2 * x2) + ... + (mn * xn) + c

Here m1, m2, m3, ..., mn -> Coefficients of the independent variables and C is the intercept

'''
# importing required libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# read the train and test dataset
dataset = pd.read_csv("sales.csv")
train_data, test_data = train_test_split(dataset, test_size=0.2, shuffle=False)

# seperate the train X,y and test X,y dataset
train_X = train_data.drop("Item_Outlet_Sales", axis=1)
train_y = train_data["Item_Outlet_Sales"]

test_X = test_data.drop("Item_Outlet_Sales", axis=1)
test_y = test_data["Item_Outlet_Sales"]

# create the linear model and train it
model = LinearRegression()
model.fit(train_X, train_y)

# coefficeints of the trained model (m)
print("Coefficient of model", model.coef_)

# intercept of the model (c)
print("Intercept of model", model.intercept_)

# predict the results
pred_y = model.predict(test_X)
print("Predictions", pred_y[0:5])

# score of the model
score = model.score(test_X, test_y)
print("Score of model", score * 100, "%")
