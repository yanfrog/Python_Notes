# math 模組

## 簡介  
`math` 模組是 Python 標準函式庫中的數學模組，提供基本的數學運算函數，包括三角函數、指數對數、取整、最大最小、公因數、常數值等。常用於基礎數學計算場景。

## 特性  
- 支援常見數學函數（例如平方根、對數、三角函數）
- 提供數學常數（例如 π、e）
- 執行速度快（使用 C 實作）
- 僅支援單一數值（不支援陣列運算，需配合迴圈或搭配 `numpy`）

## 常見函數分類

| 主題            | 函式/常數範例                                 | 功能說明                              |
|-----------------|----------------------------------------------|---------------------------------------|
| 四捨五入         | `ceil(x)`, `floor(x)`, `trunc(x)`, `round(x)` | 無條件進位、捨去小數、截斷、四捨五入     |
| 指數與對數       | `exp(x)`, `log(x[, base])`, `log10(x)`, `log2(x)` | 指數函數、對數函數（含不同底數）       |
| 開根與次方       | `sqrt(x)`, `pow(x, y)`                       | 開根號、次方                          |
| 三角函數         | `sin(x)`, `cos(x)`, `tan(x)`, `asin(x)`, `acos(x)`, `atan(x)` | 三角與反三角函數（x 為弧度）        |
| 角度轉換         | `degrees(x)`, `radians(x)`                   | 弧度與角度轉換                        |
| 絕對值與符號     | `fabs(x)`, `copysign(x, y)`                  | 取絕對值，帶符號的數值拷貝             |
| 最大公因數與最小公倍數 | `gcd(x, y)`, `lcm(x, y)`                    | 整數最大公因數、最小公倍數            |
| 排列與組合       | `perm(n, k)`, `comb(n, k)`                   | 排列（P(n, k)）、組合（C(n, k)）       |
| 數學常數         | `pi`, `e`, `tau`, `inf`, `nan`              | 常見數學常數：π、e、2π、無限大、非數值  |

## 範例

```python
import math

# 四捨五入相關
print(math.ceil(3.2))      # 4
print(math.floor(3.8))     # 3
print(math.trunc(-1.7))    # -1
print(round(3.14159, 2))   # 3.14

# 指數與對數
print(math.exp(1))         # e ≈ 2.718
print(math.log(8, 2))      # 3.0
print(math.log10(100))     # 2.0
print(math.log2(16))       # 4.0

# 次方與開根
print(math.sqrt(9))        # 3.0
print(math.pow(2, 3))      # 8.0

# 三角函數與角度轉換
print(math.sin(math.pi / 2))   # 1.0
print(math.degrees(math.pi))   # 180.0
print(math.radians(90))        # 1.5708...

# 絕對值與符號
print(math.fabs(-3.5))         # 3.5
print(math.copysign(3, -1))    # -3.0

# 最大公因數與最小公倍數
print(math.gcd(20, 12))        # 4
print(math.lcm(4, 6))          # 12

# 排列與組合（Python 3.8+）
print(math.perm(5, 2))         # 20 = P(5, 2)
print(math.comb(5, 2))         # 10 = C(5, 2)

# 常數
print(math.pi)     # 3.14159...
print(math.e)      # 2.71828...
print(math.inf)    # inf
print(math.nan)    # nan
```