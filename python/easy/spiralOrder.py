#@Time:2020/9/8 16:50
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:spiralOrder.py
__author__ = "liuAmon"

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        left,right,top,bottom=0,len(matrix[0])-1,0,len(matrix)-1
        res=[]
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            for j in range(top+1,bottom+1):
                res.append(matrix[j][right])
            if left < right and top < bottom:
                for i in range(right-1,left,-1):
                    res.append(matrix[bottom][i])
                for j in range(bottom,top,-1):
                    res.append(matrix[j][left])
            left,right,top,bottom=left+1,right-1,top+1,bottom-1
        return res

if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s=Solution()
    print(s.spiralOrder(matrix))