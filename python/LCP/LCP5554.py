# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5554.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/11/1 10:34
"""
from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hash={}
        for  p in pieces:
            for ind,i in enumerate(p):

                if ind==0:
                    hash[i]=-1
                else:
                    hash[i]=p[ind-1]
        for ind,i in enumerate(arr):
            if i in hash.keys() and   (hash[i]==-1 or (ind>0 and  arr[ind-1]==hash[i])):
                continue
            else:
                return False
        return True

if __name__=="__main__":
    arr = [2,82,79,95,28]
    pieces = [[2],[82],[28],[79,95]]
    t=Solution()
    print(t.canFormArray(arr,pieces))