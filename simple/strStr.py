#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   strStr.py    
@Contact :   utopfish@163.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/11/4 21:08   liuamon      1.0         None
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            if not needle: return 0
            if not haystack: return -1
            countMark = -1
            if len(haystack) > len(needle):
                for i in range(len(haystack) - len(needle) + 1):
                    j = 0
                    if haystack[i] == needle[j]:
                        countMark = i
                        for k in range(1, len(needle)):
                            if haystack[i + k] != needle[k]:
                                countMark = -1
                                break
                        if countMark != -1:
                            return countMark
            elif haystack == needle:
                countMark = 0
            return countMark

if __name__=="__main__":
    Test=Solution()
    print(Test.strStr("aaa","aaa"))