from sklearn.metrics import mean_squared_error
import math 

y_true = [5, 0.2, 8, -0.3]
y_pred = [6, 0.0, 7, 0.0]

MSE = mean_squared_error(y_true, y_pred)
RMSE = math.sqrt(MSE)

print(f"The RMSE is: {RMSE}")