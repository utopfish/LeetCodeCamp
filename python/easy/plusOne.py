# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:plusOne.py
#@time: 2019/10/30 19:26
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        temp=int("".join([str(x) for x in digits]))+1
        digits=[int(x) for x in str(temp)]
        return digits

if __name__=="__main__":
    Test=Solution()
    print(Test.plusOne([1,2,3]))