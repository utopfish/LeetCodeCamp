# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:beke-2.py
#@time: 2020/9/7 15:39
n=int(input())
s=input()
i=0
while s[i:].rfind(s[:i])>0 and i<n//2:
    i+=1
print(n-i+1)