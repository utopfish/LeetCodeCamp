# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:vivo02.py
#@time: 2020/9/12 20:23
s=input()
temp=0
for i in range(len(s)):
    list_s = list(s)
    list_s.pop(i)
    list_s = "".join(list_s)
    if list_s == list_s[::-1] and len(list_s) >= 1:
        print(list_s)
        break
    temp += 1
if temp >= len(s):
    print('false')