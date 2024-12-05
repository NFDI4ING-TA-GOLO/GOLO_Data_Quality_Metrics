from sklearn.metrics import r2_score

y_true = [5, 0.2, 8, -0.3]
y_pred = [6, 0.0, 7, 0.0]

R_Squared = r2_score(y_true, y_pred)

print(f"The R² is: {R_Squared}")