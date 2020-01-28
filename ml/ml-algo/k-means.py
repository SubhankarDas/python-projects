'''
ALGORITHM 6: K-MEANS CLASSIFIER

This is an unsupervised clustering algorithm, that classify data points into 'K' no. of homogeneous clusters,
that are heterogenous to other clusters. The algorithm follows thes steps to cluster data points,
1. Choose K no. of random centeroids for K no. of clusters.
2. Then assigning data points to closest of the K clusters.
3. Find new centeroids for these K clusters based on the mean value.
4. Repeat steps 2 and 3, until all the centeroids have converged i.e centeroids did not changed.

The sum of squared distances between the centeroids and data points is total sum of squared value of the solution.
This number decreases with the increase of the number of clusters i.e K
                
'''
# importing required libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# read the train and test dataset
dataset = pd.read_csv("income.csv")
train_data, test_data = train_test_split(dataset, test_size=0.2, shuffle=False)

# create the model and train with data
model = KMeans(n_clusters=5)
model.fit(train_data)

print("No. of clusters:", model.n_clusters)
print(test_data.head())

# predict the results
pred_data = model.predict(test_data)
print(pred_data[:5])

# predict the cluster for a new data point
data_point = [[65, 113, 52, 0, 1]]
pred_cluster = model.predict(data_point)
print("Data Point's Cluster No.:", pred_cluster)

# print the cluster centeroids
print("Cluster Centeroids:")
print(model.cluster_centers_)
