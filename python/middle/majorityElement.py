#@Time:2020/8/19 21:37
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:majorityElement.py
__author__ = "liuAmon"

'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

'''

from typing import List
def majorityElement(nums: List[int]) -> int:
    res = {}
    for i in nums:
        if i in res.keys():
            res[i] += 1
        else:
            res[i] = 1

    s=sorted(res.items(), key=lambda d: d[1])
    return s[-1][0]

s=[3,2,3]
print(majorityElement(s))