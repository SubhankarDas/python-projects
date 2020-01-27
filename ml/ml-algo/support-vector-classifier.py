'''
ALGORITHM 4: SUPPORT VECTOR MACHINE (SVM) / SUPPORT VECTOR CLASSIFIER

This supervised classification algorithm, plots data points in n-dimensional space, where n is the no. of
features. These data point coordinates are called Support Vectors. Now the points are divided into required
classified groups by a hyperplane. This plane/line should be such that the nearest point from the plane from 
each groups should be the farthest from each group. This line clearly divides the data points into required
groups. Now depending on this deciding line, we classify the new data point based on which side these land on. 

'''
# importing required libraries
import pandas as pd
from sklearn.svm import SVC
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

# create the model and train with data
model = SVC()
model.fit(train_X, train_y)

print(test_data.head())

# predict the results
pred_y = model.predict(test_X)
print("Survived predictions", pred_y[:5])

# score of the model
score = accuracy_score(test_y, pred_y)
print("Score of model", score * 100, "%")
