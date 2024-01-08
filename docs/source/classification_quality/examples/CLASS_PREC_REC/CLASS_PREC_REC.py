from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=0)

clf = LogisticRegression(max_iter=10000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

PRECISION = precision_score(y_test, y_pred, average='macro')
RECALL = recall_score(y_test, y_pred, average='macro')
print(f"Precision: {PRECISION}")
print(f"Recall: {RECALL}")