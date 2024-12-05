from sklearn.metrics import mean_absolute_error

y_true = [5, 0.2, 8, -0.3]
y_pred = [6, 0.0, 7, 0.0]

MAE = mean_absolute_error(y_true, y_pred)

print(f"The MAE is: {MAE}")