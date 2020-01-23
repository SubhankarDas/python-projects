'''
ALGORITHM 2: LOGISTIC REGRESSION

This is a classification algorithm, that is used to predict binary values i.e 1/0, True/False.
It classifies the results within a specific category, such as if an animal is a cat or not a cat.
The occurance is calculated based on occurance of independent factors, by fiting data into a logit function. 
This algorithm requires the dataset to contain only numerical values.

[*]     odds = occurance / not occurance = P/(1-P)
        ln(odds) = ln(P/1-P)
        logit(P) = b + b1*x1 + b2*x2 + ... + bn*xn   -> [0/1]
        
'''
# importing required libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# read the train and test dataset
dataset = pd.read_csv("titanic.csv")
train_data, test_data = train_test_split(dataset, test_size=0.2, shuffle=False)

# seperate the train X,y and test X,y dataset
train_X = train_data.drop("Survived", axis=1)
train_y = train_data["Survived"]

test_X = test_data.drop("Survived", axis=1)
test_y = test_data["Survived"]

# scale the values to units comparable to each other
scaler = StandardScaler()

train_X = scaler.fit_transform(train_X)
test_X = scaler.fit_transform(test_X)

# create the model and train with data
model = LogisticRegression()
model.fit(train_X, train_y)

print("Coefficient of model", model.coef_)
print("Intercept of model", model.intercept_)

print(test_data.head())

# predict the results
pred_y = model.predict(test_X)
print("Survived predictions", pred_y[:5])

# score of the model
score = accuracy_score(test_y, pred_y)
print("Score of model", score * 100, "%")
