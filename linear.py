#Linear Regression Example
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Dataset
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,4,5,4,5])
model = LinearRegression().fit(X, y)
y_pred = model.predict(X)

plt.scatter(X,y)
plt.plot(X,y_pred,color='red')
plt.title("Linear Regression")
plt.show()