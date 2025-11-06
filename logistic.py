import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Data
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([0,0,0,1,1])

# Train logistic regression
model = LogisticRegression().fit(X, y)

# Predict probabilities for smooth curve
X_range = np.linspace(0, 6, 300).reshape(-1,1)  # smooth x-axis values
y_prob = model.predict_proba(X_range)[:,1]      # probability of class 1

# Plot
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X_range, y_prob, color='red', label='Predicted probability')
plt.xlabel('X')
plt.ylabel('Probability of y=1')
plt.title("Logistic Regression")
plt.legend()
plt.show()
