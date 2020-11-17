# -*- coding: utf-8 -*-
"""
@Project :  PyCharm
@File    : LCP5603.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/11/15 
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if (len(word1)!=len(word2)):
            return False
        hash1={}
        hash2={}
        for i in word1:
            hash1[i]=hash1.get(i,0)+1
        for i in word2:
            hash2[i]=hash2.get(i,0)+1
        for i in hash1.keys():
            if i not in hash2.keys():
                return False
        if set(hash1.values())!=set(hash2.values()):
            return False
        return True