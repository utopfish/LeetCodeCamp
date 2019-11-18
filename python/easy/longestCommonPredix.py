# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:longestCommonPredix.py
#@time: 2019/11/5 23:08
from typeing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:  
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break           
        return s  