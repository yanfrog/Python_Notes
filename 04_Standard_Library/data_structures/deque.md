# collections — deque

## 簡介
`collections.deque` 是 Python 標準函式庫中一個雙端佇列（double-ended queue）資料結構，支援從兩端高效率的新增與刪除操作。與一般 `list` 相比，`deque` 在頭尾插入與刪除操作時間複雜度為 O(1)，非常適合用於實作佇列（Queue）、堆疊（Stack）以及其他需要頻繁在序列兩端增刪元素的場景。

## 特性
- 支援在兩端快速新增 (`append`, `appendleft`) 和刪除 (`pop`, `popleft`)
- 可設定最大長度 `maxlen`，超過時自動丟棄最舊元素，適合滑動視窗與有限長度緩存
- 支援 `rotate` 操作，可將元素整體向左或向右循環移動
- 內部使用環形緩衝區實作，空間利用率高，效率穩定
- 支援多種列表樣操作，如計數、清空、延伸等

## 主要函式與方法

| 方法               | 功能說明                                               | 時間複雜度 |
|------------------|----------------------------------------------------|----------|
| `deque(iterable=None, maxlen=None)` | 建立雙端佇列，可指定初始元素與最大長度                         | O(k)     |
| `append(x)`       | 在右端加入元素 `x`                                      | O(1)     |
| `appendleft(x)`   | 在左端加入元素 `x`                                      | O(1)     |
| `pop()`           | 從右端移除並回傳元素                                     | O(1)     |
| `popleft()`       | 從左端移除並回傳元素                                     | O(1)     |
| `extend(iterable)`| 在右端延伸加入多個元素                                    | O(k)     |
| `extendleft(iterable)` | 在左端延伸加入多個元素，元素順序為 `iterable` 的反向             | O(k)     |
| `rotate(n=1)`     | 將元素向右旋轉 `n` 位，負數向左旋轉                         | O(k)     |
| `clear()`         | 清空所有元素                                            | O(1)     |
| `count(x)`        | 計算元素 `x` 在 deque 中出現次數                            | O(n)     |
| `remove(x)`       | 移除第一次出現的元素 `x`                                  | O(n)     |

## 範例

```python
from collections import deque

# 建立 deque，預設無限長度
dq = deque([1, 2, 3])
print(dq)  # deque([1, 2, 3])

# 右端新增元素
dq.append(4)
print(dq)  # deque([1, 2, 3, 4])

# 左端新增元素
dq.appendleft(0)
print(dq)  # deque([0, 1, 2, 3, 4])

# 右端移除元素
dq.pop()
print(dq)  # deque([0, 1, 2, 3])

# 左端移除元素
dq.popleft()
print(dq)  # deque([1, 2, 3])

# 設定最大長度，超過會自動丟棄最舊元素
dq_max = deque(maxlen=3)
dq_max.extend([1, 2, 3])
print(dq_max)  # deque([1, 2, 3], maxlen=3)
dq_max.append(4)
print(dq_max)  # deque([2, 3, 4], maxlen=3) - 1 被丟棄

# 旋轉操作，向右旋轉 1 位
dq_max.rotate(1)
print(dq_max)  # deque([4, 2, 3], maxlen=3)

# 向左旋轉 2 位 (等同右旋轉 -2)
dq_max.rotate(-2)
print(dq_max)  # deque([3, 4, 2], maxlen=3)
```