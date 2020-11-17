# -*- coding: utf-8 -*-
"""
@Project :  PyCharm
@File    : beike_04.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/26 
"""

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a,b=[],[]
    for _ in range(m):
        ta,tb=map(int,input().split())
        a.append(ta)
        b.append(tb)
    if n<2:
        print(max(a))
    else:
        max_num=0
        for i in range(m):
            max_num=max(a[i]+(n-1)*b[i],max_num)
        a.sort(reverse=True)
        max_num=a[:n]
        print(max_num)