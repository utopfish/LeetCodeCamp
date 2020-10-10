# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0075sortColors.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/7 22:51
"""
"""
算法导论中三向快排问题，今天没时间了 明天继续看看
完成，方法2即为三向切分快排法，方法1仔细一看其实也是三向切分法，但并非快排
"""
from typing import  List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        size = len(nums)
        if size < 2:
            return

        zero = 0
        two = size

        i = 0

        while i < two:
            if nums[i] == 0:
                swap(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                swap(nums, i, two)


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def sort(a, lo, hi):
            if lo >= hi: return
            lt, i, gt = lo, lo + 1, hi
            v = a[lo]
            while i <= gt:
                if a[i] < v:
                    a[i], a[lt] = a[lt], a[i]
                    i += 1
                    lt += 1
                elif a[i] > v:
                    a[i], a[gt] = a[gt], a[i]
                    gt -= 1
                else:
                    i += 1
            sort(a, lo, lt - 1)
            sort(a, gt + 1, hi)

        sort(nums, 0, len(nums) - 1)