# numpy 模組

## 簡介  
`NumPy`（Numerical Python）是 Python 最重要的數值運算套件之一，提供高效能的多維陣列（ndarray）、廣播（broadcasting）、線性代數、隨機數生成、統計、向量化等功能，是科學運算、資料分析與機器學習的基礎工具。

## 特性  
- 提供固定型別、高效率的多維陣列（ndarray）
- 支援向量化運算（比 for-loop 快得多）
- 廣播機制使不同維度的陣列可進行運算
- 包含許多統計、線性代數、傅立葉轉換等函式
- 可與 C/C++、Fortran 整合，具高度擴充性

## 常見物件與功能分類

| 主題            | 函式/物件範例                           | 功能說明                         |
|-----------------|----------------------------------------|----------------------------------|
| 陣列建立         | `array`, `arange`, `linspace`, `zeros`, `ones`, `empty`, `full` | 建立各種 ndarray                |
| 陣列屬性         | `.shape`, `.ndim`, `.dtype`, `.size`   | 查詢維度、資料型別等              |
| 陣列操作         | `reshape`, `transpose`, `flatten`, `ravel`, `stack`, `concatenate`, `split` | 陣列重塑、轉置、合併、切割等     |
| 數學函數         | `sum`, `mean`, `std`, `max`, `min`, `argmax`, `argmin`, `dot`, `matmul` | 各種數學與統計運算               |
| 邏輯操作         | `where`, `any`, `all`, `logical_and`, `logical_or` | 條件運算與布林邏輯處理            |
| 廣播運算         | 隱式配對不同形狀的陣列                  | 自動展開維度進行對應元素運算       |
| 隨機數生成       | `random.rand`, `random.randn`, `random.randint`, `random.choice` | 產生各種分布的隨機數             |
| 線性代數         | `linalg.inv`, `linalg.det`, `linalg.eig`, `linalg.solve` | 矩陣反矩陣、行列式、特徵值等計算   |

## 範例

```python
import numpy as np

# 建立陣列
a = np.array([[1, 2], [3, 4]])
print(a.shape)       # (2, 2)
print(a.dtype)       # int64 (依電腦而異)

# 常用陣列建立方法
z = np.zeros((2, 3))     # 全 0
o = np.ones(shape, dtype, order) # 全 1
# shape：指定陣列的形狀（可以是整數或元組，例如 (3, 4)）
# dtype：資料型態（預設為 float）
# order：記憶體排列方式，'C' 表示 row-major（預設），'F' 表示 column-major
r = np.arange(0, 10, 2)  # [0 2 4 6 8]
l = np.linspace(0, 1, 5) # [0.   0.25 0.5  0.75 1.  ]

# 運算
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)             # [5 7 9]
print(x * y)             # [ 4 10 18]

# 廣播 (broadcasting)
m = np.array([[1], [2], [3]])
n = np.array([10, 20])
print(m + n)
# [[11 21]
#  [12 22]
#  [13 23]]

# 條件與邏輯
a = np.array([1, 2, 3, 4])
print(np.where(a > 2, a, 0))  # [0 0 3 4]
# 截斷
np.clip(array, a_min, a_max)
    # array：要處理的資料
    # a_min：下界（數值會不小於這個值）
    # a_max：上界（數值會不大於這個值）

# 線性代數
A = np.array([[1, 2], [3, 4]])
inv_A = np.linalg.inv(A)
print(np.dot(A, inv_A))      # 接近單位矩陣

# 隨機數
np.random.seed(0)
# 設定隨機種子碼
print(np.random.rand(2, 3))                     # 均勻分布
# 產生一個 2x3 的陣列，元素值在 0~1 之間，服從均勻分布（每個值出現機率相同）
print(np.random.randn(3))                       # (normal)標準常態分布
# 產生一個長度為 3 的一維陣列，元素值服從標準常態分布（平均數 0，標準差 1）
print(np.random.randint(0, 10, 5))              # (int)整數亂數
# 產生一個長度為 5 的一維陣列，元素為0 到 9（不含 10）之間的隨機整數
print(np.random.uniform(10, 20, size=5))        # 均勻分布，可任意指定範圍
# 產生 5 個 [10, 20) 區間內的隨機浮點數
print(np.random.uniform(-1, 1, size=(2, 3)))
# 產生一個 2x3 矩陣，元素落在 [-1, 1)
```

## 小提醒

- 陣列資料型態須一致，否則會自動升級（例如 int + float → float）
- `copy()` 與 `view()` 差別要特別注意，避免非預期共享記憶體
- 廣播雖方便，但需理解對齊規則：從尾部比對 shape

---
