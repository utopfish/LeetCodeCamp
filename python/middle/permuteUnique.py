#@Time:2020/9/18 10:51
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:permuteUnique.py
__author__ = "liuAmon"
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set()
        def find(path,left):
            if len(left)<=1:
                res.add(tuple(path+left))
                return
            for i in range(len(left)):
                find (path+[left[i]],left[:i]+left[i+1:])
        for i in range(len(nums)):
            find([nums[i]],nums[:i]+nums[i+1:])
        res=[list(i) for i in res]
        return res


if __name__=="__main__":
    input= [1,1,2]
    s=Solution()
    print(s.permuteUnique(input))