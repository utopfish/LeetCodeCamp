# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:c0054spirlOrder.py
#@time: 2019/11/1 12:09
from typing import List
class Solution(object):
    '''
    https://leetcode-cn.com/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode/
    '''
    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        forwardi = [1, 0, -1, 0]
        forwardj = [0, 1, 0, -1]
        x, y = 0, 0;
        flag = 0
        res = []
        if n==1:
            return " ".join(matrix[0])
        elif m==1:
            return " ".join([i[0] for i in matrix])
        while (n > 1 and m >1 ):
            if flag % 2 == 0:
                for i in range(n - 1):
                    res.append(matrix[x][y])
                    x += forwardi[flag]
                    y += forwardj[flag]
                if flag == 2:
                    n -= 1
            else:
                for i in range(m - 1):
                    res.append(matrix[x][y])
                    x += forwardi[flag]
                    y += forwardj[flag]
                if flag == 1:
                    m -= 1
            flag += 1
            flag = flag % 4
        return res

if __name__=="__main__":
    Test=Solution()
    print(Test.spiralOrder2(
        [
            ['10','20']
        ]))