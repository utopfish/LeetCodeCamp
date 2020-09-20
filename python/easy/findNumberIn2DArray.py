#@Time:2020/9/20 17:05
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:findNumberIn2DArray.py
__author__ = "liuAmon"

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            else: return True
        return False
