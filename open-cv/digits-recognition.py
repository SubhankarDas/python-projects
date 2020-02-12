import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as pt

TEST_CASE_INDEX = 191  # test case to be displayed

# read dataset and split train and test datasets
dataset = pd.read_csv("digits.csv")  # digit recognizer data set from kaggle

train_data, test_data = train_test_split(dataset, test_size=0.2, shuffle=False)

train_X = train_data.drop("label", axis=1)
train_labels = train_data["label"]

test_X = test_data.drop("label", axis=1)
test_labels = test_data["label"]

# create model and train with data
model = DecisionTreeClassifier()
model.fit(train_X, train_labels)

# predict labels for test set and calculate accuracy score
predicted_labels = model.predict(test_X)
score = accuracy_score(test_labels, predicted_labels)

print("Accuracy Score:", score*100)

print("Actual Labels    :", test_labels.values[:10])
print("Predicted Labels :", predicted_labels[:10])

# pick the test case from set, predict label and display
test_case = test_X.values[TEST_CASE_INDEX]
lbl = model.predict([test_case])
print("Predicted Digit  :", lbl)

test_case.shape = (28, 28)
pt.imshow(255-test_case, cmap="gray")
pt.show()
