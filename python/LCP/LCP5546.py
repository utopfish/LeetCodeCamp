# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5546.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/25 10:36
"""
from typing import List
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        hash={}
        for ind,i in enumerate(keysPressed):
            if ind==0:
                hash[i]=hash.get(i,0)+releaseTimes[ind]
            else:
                hash[i]=max(hash.get(i,0),releaseTimes[ind]-releaseTimes[ind-1])
        res=sorted(hash.items(),key=lambda x:x[1],reverse=True)
        return res[0][0]

if __name__=="__main__":
    s=Solution()
    a="cbcd"
    b=[9,29,49,50]
    print(s.slowestKey(b,a))