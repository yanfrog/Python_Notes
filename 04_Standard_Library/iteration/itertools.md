# itertools 模組

## 簡介  
`itertools` 提供高效能、記憶體友善的迭代器工具，可用於處理排列、組合、累加、無限序列等功能，廣泛用於資料處理、演算法優化。

## 特性  
- 所有函式都回傳「疊代器（iterator）」，可搭配 `for` 迴圈或轉為 `list` 使用  
- 記憶體使用量低，適合處理大型資料或無限序列  
- 提供排列、組合、連接、篩選、累計等常見操作  

## 主要函式與時間複雜度

| 函式名稱            | 功能說明                             | 時間複雜度 (生成單一結果) | 空間複雜度 |
|---------------------|--------------------------------------|----------------------------|-------------|
| `count(start=0, step=1)` | 產生無限遞增序列                    | O(1)                       | O(1)        |
| `cycle(iterable)`   | 無限重複輸入序列                     | O(1) 每次產生               | O(n) 儲存序列 |
| `repeat(obj, times=None)` | 重複給定元素指定次數（或無限次）    | O(1)                       | O(1)        |
| `accumulate(iterable, func=operator.add)` | 累計操作（預設加總）        | O(n)                       | O(1)        |
| `chain(*iterables)` | 串接多個序列                        | O(1) 每次產生               | O(1)        |
| `combinations(iterable, r)` | 不重複組合                         | O(nCr)                     | O(r)        |
| `permutations(iterable, r=None)` | 排列                         | O(nPr)                     | O(r)        |
| `product(*iterables, repeat=1)` | 笛卡兒積                       | O(k^n)                     | O(n)        |
| `groupby(iterable, key=None)` | 依條件分組（連續相同元素歸類） | O(n)                       | O(1)        |
| `islice(iterable, start, stop, step=1)` | 切片操作類似 list 的 slice   | O(1) 每次產生               | O(1)        |
| `filterfalse(predicate, iterable)` | 過濾不符合條件的元素          | O(n)                       | O(1)        |
| `takewhile(predicate, iterable)` | 條件為真時持續取出            | O(k)（k為滿足條件元素數）   | O(1)        |
| `dropwhile(predicate, iterable)` | 條件為真時跳過，之後全部保留  | O(k) 跳過元素數             | O(1)        |

## 常見範例

```python
import itertools

# count：無限序列
for i in itertools.count(10, 2):
    print(i)
    if i > 20:
        break  # 請務必搭配終止條件

# cycle：無限重複
cyc = itertools.cycle(['A', 'B', 'C'])
for _ in range(5):
    print(next(cyc))  # A B C A B

# repeat：重複元素
for i in itertools.repeat('Hello', 3):
    print(i)

# accumulate：累計和
nums = [1, 2, 3, 4]
print(list(itertools.accumulate(nums)))  # [1, 3, 6, 10]

# combinations：組合
for c in itertools.combinations('ABC', 2):
    print(c)

# permutations：排列
for p in itertools.permutations('ABC', 2):
    print(p)

# product：笛卡兒積
for prod in itertools.product('AB', '12'):
    print(prod)

# groupby：分組
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4)]
for k, group in itertools.groupby(data, key=lambda x: x[0]):
    print(k, list(group))

# islice：切片
print(list(itertools.islice(range(10), 2, 7, 2)))  # [2, 4, 6]
```
