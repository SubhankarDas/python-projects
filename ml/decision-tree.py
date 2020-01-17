import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")

#--- DECISION TREE ---#
# to create a decision tree all the data should be numerical.
# hence we need to map the non-numerical data to numerical values.
d = {'UK': 0, 'USA': 1, 'N': 2}
# pandas map func. takes a dictionary to map values
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']  # deciding features

X = df[features]
y = df['Go']


dtree = DecisionTreeClassifier()  # decision tree model
dtree = dtree.fit(X, y)  # fit data set


# draw the decision tree, write as a PNG and show in a plot
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('decisiontree.png')

img = pltimg.imread('decisiontree.png')
imgplot = plt.imshow(img)
plt.show()


# prediction: should I go see a show starring a 40 years old American comedian,
# with 10 years of experience, and a comedy ranking of 7?
print(dtree.predict([[40, 10, 7, 1]]))  # [1] = YES   [0] = NO
