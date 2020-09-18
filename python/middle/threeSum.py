#@Time:2020/9/11 21:25
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:threeSum.py
__author__ = "liuAmon"
from typing import List
#方法超时
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


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res

if __name__=="__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    s=Solution2()
    print(s.threeSum(nums))