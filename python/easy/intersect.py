# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:intersect.py
#@time: 2019/11/8 15:59
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []
        if len(nums1) < len(nums2):
            nums3 = nums1
            nums4 = nums2
        else:
            nums3 = nums2
            nums4 = nums1
        for _, item in enumerate(nums3):
            if item in nums4:
                res.append(item)
                nums4.remove(item)
        return res