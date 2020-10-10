# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c0018fourSum.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/10 11:20
"""

from typing import List
#这种递归本质上还是循环遍历，并不能降低时间复杂度，对与这种使用排序+双指针能将O(n^2)变为O(nlogn+n),同时加上对一些边界情况的剪枝，能近似为O(n),

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        def find(deep,path,index):
            for i in range(index+1,n):
                if deep==3 and sum(path)+nums[i]==target and path+[nums[i]] not in res:
                    res.append(path+[nums[i]])
                elif  deep>3:
                    break
                else:
                    find(deep+1,path+[nums[i]],i)
            return
        for i in range(n-3):
            find(1,[nums[i]],i)
        return res


class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        if n < 4:
            return res
        for fir in range(n-3):
            if fir > 0 and nums[fir] == nums[fir - 1]:
                continue
            if nums[fir] + nums[fir + 1] + nums[fir + 2] + nums[fir + 3] > target:
                break
            if nums[fir] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue
            for sec in range(fir + 1, n-2):
                if sec > fir + 1 and nums[sec] == nums[sec - 1]:
                    continue
                if nums[fir] + nums[sec] + nums[sec + 1] + nums[sec + 2] > target:
                    break
                if nums[fir] + nums[sec] + nums[n - 1] + nums[n - 2] < target:
                    continue
                left, right = sec + 1, n - 1
                while left < right:
                    total = nums[fir] + nums[sec] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[fir], nums[sec], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left+=1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right-=1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1

        return res

if __name__=="__main__":
    nums = [1,-2,-5,-4,-3,3,3,5]
    target=-11
    s=Solution2()
    print(s.fourSum(nums,target))