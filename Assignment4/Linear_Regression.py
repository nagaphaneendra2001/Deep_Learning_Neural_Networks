# Simple Linear Regression
# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as sk

#Importing the datasets
dataset = pd.read_csv("Salary_Data.csv")

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1]

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Fitting Simple Linear Regression to the training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set result ￼

y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error
meansquareerror = mean_squared_error(y_true=y_test,y_pred=y_pred)
print("Mean Square Error:",meansquareerror)

# Visualizing the training set results

viz_train = plt
viz_train.scatter(X_train, y_train, color='green')
viz_train.plot(X_train, regressor.predict(X_train), color='black')
viz_train.title('Training set')
viz_train.xlabel('Years Experience')
viz_train.ylabel('Salary')
viz_train.show()

viz_test = plt
viz_test.scatter(X_test, y_test, color='green')
viz_test.plot(X_train, regressor.predict(X_train), color='black')
viz_test.title('Test set')
viz_test.xlabel('Years Experience')
viz_test.ylabel('Salary')
viz_test.show()