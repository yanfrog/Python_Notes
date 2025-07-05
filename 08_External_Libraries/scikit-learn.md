# scikit-learn 模組

## 簡介

`scikit-learn` 是 Python 最廣泛使用的傳統機器學習（非神經網路模型）套件，提供簡單統一的 API，滿足:

- 資料前處理
- 特徵工程
- 各類機器學習模型（分類、回歸、聚類）
- 模型評估與交叉驗證
- 管線與模型選擇

## 特性

- 支援大量機器學習演算法（SVM、Random Forest、KNN、Naive Bayes 等）
- 一致的 API 設計（fit / predict / transform）
- 易於與 NumPy、Pandas、Matplotlib 搭配使用
- 適用於小至中程規模資料集
- 非深度學習，無須 GPU 支援

---

## 安裝

```bash
pip install scikit-learn
```

---

## 常見使用流程

兩個經典資料集，用於分類任務實作：
- **Iris 花朵分類**：預測鳶尾花屬於哪一個品種，依據其花萼與花瓣的長度與寬度。
  - **資料集結構**：共 150 筆樣本，4 個數值特徵：`sepal length`、`sepal width`、`petal length`、`petal width`
  - **目標欄位 y**：類別標籤 0（Setosa）、1（Versicolor）、2（Virginica）

- **手寫數字辨識**：根據圖片像素值判斷數字 0 到 9。
  - **資料集結構**：共 1797 筆樣本，每筆是 8x8 的灰階圖像，共 64 維特徵（flattened）
  - **目標欄位 y**：數字 0～9 的整數標籤



### 範例 1：Iris 花朵分類（`load_iris()`）

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. 讀取資料
X, y = load_iris(return_X_y=True)

# 2. 切分資料集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. 建立模型
clf = RandomForestClassifier()

# 4. 訓練模型
clf.fit(X_train, y_train)

# 5. 預測
y_pred = clf.predict(X_test)

# 6. 評估模型
print("[Iris] Accuracy:", accuracy_score(y_test, y_pred))
```

### 範例 2：手寫數字辨識（`load_digits()`）

```python
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
```

---

## 常見模組分類

scikit-learn 以模組化方式設計，以下為常見 `sklearn.<模組>` 子模組與其用途：

| 模組名稱                     | 用途簡述                                           | 範例函式與類別                        |
|------------------------------|----------------------------------------------------|----------------------------------------|
| `sklearn.datasets`           | 提供內建資料集與資料讀取函式                      | `load_iris()`, `load_digits()`        |
| `sklearn.preprocessing`      | 資料前處理與標準化                                | `StandardScaler()`, `LabelEncoder()`  |
| `sklearn.model_selection`    | 資料切分、交叉驗證、參數搜尋                      | `train_test_split()`, `GridSearchCV()`|
| `sklearn.linear_model`       | 線性模型（回歸、分類）                            | `LinearRegression()`, `LogisticRegression()` |
| `sklearn.ensemble`           | 集成學習模型（如隨機森林、投票器等）             | `RandomForestClassifier()`, `VotingClassifier()` |
| `sklearn.svm`                | 支援向量機模型                                    | `SVC()`, `SVR()`                       |
| `sklearn.tree`               | 決策樹模型                                        | `DecisionTreeClassifier()`            |
| `sklearn.neighbors`          | 鄰近演算法（KNN）                                 | `KNeighborsClassifier()`              |
| `sklearn.cluster`            | 聚類模型（無監督學習）                            | `KMeans()`, `DBSCAN()`                |
| `sklearn.naive_bayes`        | 樸素貝氏分類器                                    | `GaussianNB()`, `MultinomialNB()`     |
| `sklearn.metrics`            | 模型評估指標與混淆矩陣                            | `accuracy_score()`, `confusion_matrix()` |
| `sklearn.pipeline`           | 管線組合：將多個步驟（前處理 + 模型）串接成流程   | `Pipeline()`, `make_pipeline()`       |
| `sklearn.feature_selection`  | 特徵選擇                                          | `SelectKBest()`, `RFE()`              |
| `sklearn.decomposition`      | 維度縮減（如主成分分析 PCA）                     | `PCA()`, `TruncatedSVD()`             |

---

## Pipeline 範例（標準化 + 模型）

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC())
])

pipe.fit(X_train, y_train)
preds = pipe.predict(X_test)
```

---

## 參考資源

- 官方文件：[https://scikit-learn.org/](https://scikit-learn.org/)
- 教學範例：[https://scikit-learn.org/stable/tutorial/index.html](https://scikit-learn.org/stable/tutorial/index.html)