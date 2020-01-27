'''
ALGORITHM 6: KNN (K- NEAREST NEIGHBORS) CLASSIFIER

This algorithm can be used for both classification and regression. The approach is simple, plot all the data
points and the new data points are voted by 'k' no. of nearest neighbors and the points are assigned to the class
with the majority of the votes. If k=1, new data point is assigned to the class of the nearest neighbor hence the
selection of K times can be difficult in some cases. KNN is computationally expensive.

[*]     Distance between two data points (D) = Square Root of ((x2-x1)^2 + (y2-y1)^2)   [Euclidean Distance]
                
'''
# importing required libraries
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# read the train and test dataset
dataset = pd.read_csv("titanic.csv")
train_data, test_data = train_test_split(dataset, test_size=0.2, shuffle=False)

# seperate the train X,y and test X,y dataset
train_X = train_data.drop("Survived", axis=1)
train_y = train_data["Survived"]

test_X = test_data.drop("Survived", axis=1)
test_y = test_data["Survived"]

# create the model and train with data
model = KNeighborsClassifier()
model.fit(train_X, train_y)

print("No. of neighbors used to predict:", model.n_neighbors)
print(test_data.head())

# predict the results
pred_y = model.predict(test_X)
print("Survived predictions", pred_y[:5])

# score of the model
score = accuracy_score(test_y, pred_y)
print("Score of model", score * 100, "%")
