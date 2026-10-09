import numpy as np
from sklearn.linear_model import LinearRegression

# Independent variable
X = np.array([
    [2],
    [4],
    [6],
    [8],
    [10]
])

# Dependent variable
y = np.array([
    40,
    50,
    65,
    80,
    90
])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict marks for 7 hours
prediction = model.predict([[7]])

print("Predicted Marks:", prediction[0])

print("Slope:", model.coef_[0])

print("Intercept:", model.intercept_)