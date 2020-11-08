# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5562.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/11/8 10:44
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        hash={}
        for i in s:
            hash[i]=hash.get(i,0)+1
        length = [0] *(max(hash.values())+1)
        for ind,v in enumerate(hash.values()):
            length[v]+=1
        count=0
        for i in range(len(length)-1,-1,-1):
            while length[i]>1:
                for j in range(i-1,-1,-1):
                    if j == 0:
                        length[j]=0
                        length[i]-=1
                        count+=(i-j)
                    elif length[j]==0:
                        length[j]=1
                        length[i]-=1
                        count+=(i-j)
                        break

        return count


if __name__=="__main__":
    s=Solution()
    print(s.minDeletions("bbcebab"))
