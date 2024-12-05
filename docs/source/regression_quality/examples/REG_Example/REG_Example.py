import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Generate sample data
X = np.random.rand(100, 1)
y = 3 * X + 4 + np.random.randn(100, 1)

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Calculate the evluation metrics
MAE = mean_absolute_error(y, y_pred)
MSE = mean_squared_error(y, y_pred)
RMSE = math.sqrt(MSE)
R_Squared = r2_score(y, y_pred)

print(f"MSE: {MSE}")
print(f"RMSE: {RMSE}")
print(f"MAE: {MAE}")
print(f"R²: {R_Squared}")

# Plot
plt.scatter(X, y, label='Actual values')
plt.plot(X, y_pred, color='red', label='Predicted values')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Actual VS. Predicted values')
plt.show()

