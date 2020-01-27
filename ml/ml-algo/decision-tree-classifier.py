'''
ALGORITHM 3: DECISION TREE CLASSIFIER

This algorithm can be used for both classification (categorical data) and regression (continuous data).
Decision trees are created using hueristic recursive partitioning also known as divide-and-conquer.
The algorithm splits the dataset into smaller subsets and continuous to split until the subsets are sufficiently
homogeneous or meet another stopping criteria.

'''
# importing required libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
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
model = DecisionTreeClassifier()
model.fit(train_X, train_y)

print(test_data.head())

# predict the results
pred_y = model.predict(test_X)
print("Survived predictions", pred_y[:5])

# score of the model
score = accuracy_score(test_y, pred_y)
print("Score of model", score * 100, "%")
