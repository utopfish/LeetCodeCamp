# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5555.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/11/1 11:30
"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        def dfs(n):
            if n==1:
                return 5,1,1,1,1,1
            n,a,e,i,o,u=dfs(n-1)
            new_n=a*5+e*4+i*3+o*2+u
            return new_n,a,e+a,a+e+i,a+e+i+o,a+e+i+o+u
        n,a,e,i,o,u=dfs(n)
        return n

if __name__=="__main__":
    s=Solution()
    print(s.countVowelStrings(33))