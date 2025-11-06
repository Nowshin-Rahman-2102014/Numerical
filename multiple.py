# Multiple Regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([3, 5, 7, 9])

model = LinearRegression().fit(X, y)
y_pred = model.predict(X)

plt.scatter(range(len(y)), y, label='Actual')
plt.plot(range(len(y)), y_pred, color='red', label='Predicted')
plt.title("Multiple Regression")
plt.legend()
plt.show()
