#@Time:2020/9/9 16:56
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:minNumber.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort(arr):
            if len(arr)<2:
                return arr
            pivot=arr[0]
            less=[]
            greater=[]
            for i in arr[1:]:
                if (i+pivot)<(pivot+i):
                    less.append(i)
                else:
                    greater.append(i)
            return sort(less)+[pivot]+sort(greater)
        nums=[str(i) for i in nums]
        res=sort(nums)
        return "".join(res)

if __name__=="__main__":
    input=[3,30,34,5,9]
    s=Solution()
    print(s.minNumber(input))