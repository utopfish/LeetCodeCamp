# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:dominantIndex.py
#@time: 2019/10/30 18:59
from typing import List
import copy
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxnumber=max(nums)
        temp=copy.deepcopy(nums)
        nums.remove(maxnumber)
        secondnumber=max(nums)
        if maxnumber>=secondnumber*2:
            return temp.index(maxnumber)
        else:
            return -1
if __name__=="__main__":
    Test=Solution()
    print(Test.dominantIndex([1, 2, 3, 4]))