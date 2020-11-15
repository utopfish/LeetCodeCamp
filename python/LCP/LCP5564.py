# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5564.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/11/8 12:12
"""
from typing import List
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def add(x: int) -> None:
            # 将x插入到树状数组中
            while x < n:
                nums[x] += 1
                x += (x & -x)

        def getSum(x: int) -> int:
            # 求出小于等于x的元素个数
            res = 0
            while x > 0:
                res += nums[x]
                x -= (x & -x)
            return res

        # 创建树状数组
        n = max(instructions) + 1
        nums = [0 for _ in range(n)]
        # res为总代价
        res = 0
        # cnt为当前存在元素
        cnt = 0
        for i in instructions:
            # getSum(i-1)求比自己小的元素个数
            # cnt - getSum(i)求比自己大的元素个数
            res = (res + min(getSum(i - 1), cnt - getSum(i))) % (10 ** 9 + 7)
            add(i)
            cnt += 1
        return res

if __name__=="__main__":
    instructions = [1, 5, 6, 2]
    s=Solution()
    print(s.createSortedArray(instructions))