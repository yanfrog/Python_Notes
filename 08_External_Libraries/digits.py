from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. 讀取資料
X, y = load_digits(return_X_y=True)

# 2. 切分資料集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. 建立模型
clf = RandomForestClassifier()

# 4. 訓練模型
clf.fit(X_train, y_train)

# 5. 預測
y_pred = clf.predict(X_test)

# 6. 評估模型
print("[Digits] Accuracy:", accuracy_score(y_test, y_pred))