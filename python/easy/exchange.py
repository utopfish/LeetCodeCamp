#@Time:2020/9/2 15:42
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:exchange.py
__author__ = "liuAmon"
from typing import List
def exchange(nums: List[int]) -> List[int]:
    i,j=0,len(nums)-1
    while i<j:
        while nums[i]%2==1:
            i+=1
        while nums[j]%2==0:
            j-=1
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        i+=1
        j-=1
    return nums
print(exchange([1,2,3,4]))
