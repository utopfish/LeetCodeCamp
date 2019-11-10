# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:rotate.py
#@time: 2019/11/10 12:09
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

                # reverse each row
        for i in range(n):
            matrix[i].reverse()
        return matrix

if __name__=="__main__":
    Test=Solution()
    print(Test.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))