from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=0)

clf = LogisticRegression(max_iter=10000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# One-vs-One approach
y_prob = clf.predict_proba(X_test)
AU_ROC = roc_auc_score(y_test, y_prob, multi_class='ovo', average='macro')
print(f"AU-ROC: {AU_ROC}")