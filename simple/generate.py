# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:generate.py
#@time: 2019/11/2 12:32
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1: return []
        result = []

        for i in range(numRows):
            if i == 0:
                result.append([1])
            else:
                temp = [1]
                for j in range(i):
                    if j != i - 1:
                        temp.append(result[i - 1][j] + result[i - 1][j + 1])
                    else:
                        temp.append(1)
                result.append(temp)
        return result