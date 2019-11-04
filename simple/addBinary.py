# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:addBinary.py
#@time: 2019/11/3 12:04
class Solution2:
    def addBinary(self, a, b) -> str:
        #p记录进位
        r, p = '', 0
        d = len(b) - len(a)
        a = '0' * d + a
        b = '0' * -d + b
        for i, j in zip(a[::-1], b[::-1]):
            s = int(i) + int(j) + p
            r = str(s % 2) + r
            p = s // 2
        return '1' + r if p else r
class Solution:
    def addBinary(self,a,b):
        r,p='',0
        d=len(a)-len(b)
        a='0'*(-d)+a
        b='0'*d+b
        #[::-1]为数组逆序
        for i,j in zip(a[::-1],b[::-1]):
            s=int(i)+int(j)+p
            r=str(s%2)+r
            p=s//2
        return '1'+r if p else r
if __name__=="__main__":
    Test=Solution()
    print(Test.addBinary("11","1"))