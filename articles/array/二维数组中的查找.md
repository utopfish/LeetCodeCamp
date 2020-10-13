###  剑指 Offer 04. 二维数组中的查找
#### 标签 
简单 查找
#### 描述

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


#### 示例
```
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。给定 target = 20，返回 false。

```

#### 限制
0 <= n <= 1000
0 <= m <= 1000
#### 代码
从左下开始判断
```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            else: return True
        return False
```
#### 执行结果

执行用时：40 ms, 在所有 Python3 提交中击败了94.46% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了57.61% 的用户