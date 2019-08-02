# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Importing the dataset
dirty_train_dataset = pd.read_csv('data/train.csv')
dirty_test_dataset = pd.read_csv('data/test.csv')
train_dataset = dirty_train_dataset.dropna() 
test_dataset = dirty_test_dataset.dropna() 

X_train = train_dataset.iloc[:, :1].values
y_train = train_dataset.iloc[:, 1].values

X_test = test_dataset.iloc[:, :1].values
y_test = test_dataset.iloc[:, 1].values

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

#preserve the model
pickle.dump(regressor, open('pickled-model', 'wb'))

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Accuracy
score = regressor.score(X_test, y_test)
print("Accuracy", score)