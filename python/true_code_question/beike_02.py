# -*- coding: utf-8 -*-
"""
@Project :  PyCharm
@File    : beike_02.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/26 
"""
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    l,r=0,n-1
    res='no'
    while l<r:
        if arr[l]*arr[r]>m:
            r-=1
        elif arr[l]*arr[r]<m:
            l+=1
        else:
            res='yes'
            break
    print(res)