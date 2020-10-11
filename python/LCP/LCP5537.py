# -*- coding: utf-8 -*-
"""
@Project : LeetCodeCamp
@File    : LCP5537.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/11 10:56
"""



class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        left,right=0,len(a)-1
        while left<right:
            if a[left]==b[right] or a[right]==b[left] or a[left]==a[right] or b[left]==b[right] :
                left+=1
                right-=1
            else:
                return False
        return True
class Solution2:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        left,right=0,len(a)
        while left<=right:
            tmp1=a[:left]+b[left:]
            tmp2=b[:right]+a[right:]
            if tmp1==tmp1[::-1] or tmp2==tmp2[::-1]:
                return True
            left+=1
            right-=1
        return False
if __name__=="__main__":
    a="pvhmupgqeltozftlmfjjde"
    b="yjgpzbezspnnpszebzmhvp"
    # a="ulacfd"
    # b="jizalu"
    s=Solution()
    print(s.checkPalindromeFormation(a,b))