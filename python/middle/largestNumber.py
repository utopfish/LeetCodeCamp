#@Time:2020/9/18 12:37
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:largestNumber.py
__author__ = "liuAmon"
from typing import List

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=map(str,nums)
        nums=sorted(nums,key=cmp_to_key(lambda x,y:int(y+x)-int(x+y)))
        res= "".join(nums).lstrip('0')
        return res or '0'

if __name__=="__main__":
    input=[10,2]
    s=Solution()
    print(s.largestNumber(input))