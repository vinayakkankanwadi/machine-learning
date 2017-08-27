# import numpy
import numpy as np

# import DecisionTreeClassifier
from sklearn import tree

# import dataset
from sklearn.datasets import load_iris
iris = load_iris()

# print feature names
# print(iris.feature_names)
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

# print species names
# print(iris.target_names)
# ['setosa' 'versicolor' 'virginica']

# print features of first item in dataset
# print(iris.data[0])

# print species of first item in dataset
# print(iris.target[0])

# iterate over all items in dataset
# for i in range(len(iris.target)):
#	print("Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i]))

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis = 0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
