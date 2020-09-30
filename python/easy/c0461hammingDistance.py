# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:c0461hammingDistance.py
#@time: 2020/9/22 11:00
"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
      ↑   ↑

"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        t=x^y
        res=0
        while t>0:
            res+=t&1
            t>>=1
        return res

#此法时间耗时更少，有点想不通
class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        num = 0
        res = []
        while x != 0 or y != 0:
            res.append((x%2, y%2))
            x //= 2
            y //= 2
        for xii, yii in res:
            if xii != yii:
                num += 1
        return num