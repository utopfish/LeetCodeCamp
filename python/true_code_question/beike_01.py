# -*- coding: utf-8 -*-
"""
@Project :  PyCharm
@File    : beike_01.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/26 
"""
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if x!=y and x!=z and y!=z:
        print("NO")
    else:
        tmp=[x,y,z]
        tmp.sort()
        if tmp[2]==tmp[1]:
            print("YES")
            print(tmp[2],tmp[0],tmp[0]-1)
        elif sum(tmp)//3==tmp[1]:
            print("YES")
            print(x,y,z)

