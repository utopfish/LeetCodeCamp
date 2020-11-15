# -*- coding: utf-8 -*-
"""
@Project :  PyCharm
@File    : LCP5602.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/11/15 
"""
from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        queue=set([(x,-1,len(nums))])
        min_step=float('inf')
        length=len(nums)
        while queue!=set():
            cur_x,cur_left,cur_right=queue.pop()
            if cur_left>=cur_right:
                continue
            if cur_x==0:
                min_step=min(min_step,cur_left+1+(len(nums)-cur_right))
            if cur_left+1 <length and nums[cur_left+1]<=cur_x:
                # if (cur_x-nums[cur_left+1],cur_left+1,cur_right) not in queue:
                    queue.add((cur_x-nums[cur_left+1],cur_left+1,cur_right))
            if cur_right-1 >-1 and nums[cur_right-1]<=cur_x:

                    queue.add((cur_x-nums[cur_right-1],cur_left,cur_right-1))
        return min_step if min_step!=float('inf') else -1
if __name__=="__main__":
    nums=[1,1]
    x=3
    s=Solution()
    print(s.minOperations(nums,x))