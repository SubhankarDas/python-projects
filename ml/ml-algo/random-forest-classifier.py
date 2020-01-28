'''
ALGORITHM 8: RANDOM FOREST

This algorithm uses a collection of decision trees, each tree classifies new data points based on
attributes and votes for a class. The algorithm chooses the final class based on the most no. of
votes over all of the trees in the forest. If there are N no. of training cases, N no. of random
sampling will be done to grow the trees.

'''
# importing required libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
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
model = RandomForestClassifier()
model.fit(train_X, train_y)

print(test_data.head())

# predict the results
pred_y = model.predict(test_X)
print("Survived predictions", pred_y[:5])

# score of the model
score = accuracy_score(test_y, pred_y)
print("Score of model", score * 100, "%")
