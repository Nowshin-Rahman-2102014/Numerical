# Stochastic Gradient Descent (SGD)
from sklearn.linear_model import SGDRegressor

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,4,5,4,5])

model = SGDRegressor(max_iter=1000, tol=1e-3).fit(X,y)
y_pred = model.predict(X)

plt.scatter(X,y)
plt.plot(X,y_pred,color='red')
plt.title("SGD Regression")
plt.show()