# bisect 模組

## 簡介
`bisect` 模組提供維持已排序的 `List` 的二分搜尋與插入功能，可用於快速查找插入位置。

## 主要函式

| 函式名稱       | 功能說明                          | 時間複雜度    | 空間複雜度 | 備註                       |
|--------------|-------------------------------|------------|----------|--------------------------|
| bisect_left  | 在排序列表中找到插入點，插入點在相同值的左邊 | O(log n)   | O(1)     | 二分搜尋定位插入位置              |
| bisect_right | 在排序列表中找到插入點，插入點在相同值的右邊 | O(log n)   | O(1)     | 同上                      |
| bisect       | 同 bisect_right 的別名              | O(log n)   | O(1)     | 同上                      |
| insort_left  | 以 bisect_left 方式插入元素           | O(n)       | O(1)     | 找位置 O(log n) + 插入列表 O(n) |
| insort_right | 以 bisect_right 方式插入元素          | O(n)       | O(1)     | 同上                      |
| insort       | 同 insort_right 的別名              | O(n)       | O(1)     | 同上                      |

## 範例

```python
import bisect

lst = [1, 3, 4, 4, 5]

# 找插入位置
pos = bisect.bisect_left(lst, 4)
print(pos)  # 2 (4的最左邊位置)

pos = bisect.bisect_right(lst, 4)
print(pos)  # 4 (4的最右邊位置)

# 插入元素
bisect.insort(lst, 2)
print(lst)  # [1, 2, 3, 4, 4, 5]
```