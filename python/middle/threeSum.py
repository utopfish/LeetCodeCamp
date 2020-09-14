#@Time:2020/9/11 21:25
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:threeSum.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def dsf(path,t,index,deep):
            for i in range(index+1,len(nums)):
                if t+nums[i]>0 or deep>2:
                    break
                if t+nums[i]==0 and deep==2 and path+[nums[i]] not in res:
                    res.append(path+[nums[i]])
                    break
                elif t+nums[i]<=0:
                    dsf(path+[nums[i]],t+nums[i],i,deep+1)

        for i in range(len(nums)):
            if nums[i]>0:
                break
            else:
                dsf([nums[i]],nums[i],i,1)
        return res

if __name__=="__main__":
    nums = [0,0,0]
    s=Solution()
    print(s.threeSum(nums))