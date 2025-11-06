# Polynomial Regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([1,4,9,16,25])

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression().fit(X_poly, y)
y_pred = model.predict(X_poly)

plt.scatter(X,y)
plt.plot(X,y_pred,color='red')
plt.title("Polynomial Regression")
plt.show()