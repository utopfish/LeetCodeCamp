# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:c0997sortedSquares.py
#@time: 2020/10/16 23:01


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(nums**2 for nums in A)