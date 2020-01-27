'''
ALGORITHM 5: NAIVE BAYES CLASSIFIER

This classifer is a family of algorithms, which assumes all the features are independently contributing to the
presence of the event and not being related to any other of the features.

[*]     P(A/B) = (P(B/A) P(A)) / P(B)

P(occurance of A after B has occured) = (P(occurance of B after A has occured) * P(A)) / P(B)

Ex.: P(No Buy/Weekdays) = (P(Weekdays/No Buy) * P(No Buy)) / P(Weekdays)

[*]     P(A/BCD) = (P(B/A) * P(C/A) * P(D/A) * P(A))/(P(B) * P(C) * P(D))
                
'''
# importing required libraries
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
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
model = MultinomialNB()
model.fit(train_X, train_y)

print(test_data.head())

# predict the results
pred_y = model.predict(test_X)
print("Survived predictions", pred_y[:5])

# score of the model
score = accuracy_score(test_y, pred_y)
print("Score of model", score * 100, "%")
