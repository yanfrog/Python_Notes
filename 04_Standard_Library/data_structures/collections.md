# collections 模組

## 簡介
`collections` 是 Python 標準函式庫中提供多種高效能的容器資料型態模組，補強內建容器的功能。

## 主要類別與函式

| 類別/函式          | 功能說明                                |
|-------------------|-------------------------------------|
| namedtuple        | 建立具名稱欄位的 tuple 子類別              |
| deque             | 雙端佇列，支援從兩端快速新增/刪除          |
| ChainMap          | 多個 dict 的串接，查詢時依序尋找            |
| Counter           | 元素計數器，類似多重集合                    |
| OrderedDict       | 有序字典，保留插入順序（Python 3.7+ dict 已保留順序） |
| defaultdict       | 帶有預設值工廠函式的字典                    |
| UserDict          | 可擴充的字典類別                          |
| UserList          | 可擴充的串列類別                          |
| UserString        | 可擴充的字串類別                          |

## 範例

```python
from collections import deque, Counter, namedtuple

# deque 範例
d = deque([1, 2, 3])
d.appendleft(0)
print(d)  # deque([0, 1, 2, 3])

# Counter 範例
c = Counter("abracadabra")
print(c)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# namedtuple 範例
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
```