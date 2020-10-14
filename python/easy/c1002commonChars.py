# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : c1002commonChars.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/14 13:55
"""
from typing import List
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        hash={}
        for i in A[0]:
            hash[i]=hash.get(i,0)+1
        for ind,s in enumerate(A[1:]):
            tmp={}
            for i in s:
                if i in hash.keys():
                    tmp[i]=tmp.get(i,0)+1
            for key in hash.keys():
                if key in tmp.keys():
                    hash[key]=min(hash.get(key),tmp.get(key))
                else:
                    hash[key]=0
        res=[]
        for i in hash.items():
                for _ in range(i[1]):
                    res.append(i[0])
        return res