# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:al_01.py
# n, m = map(int, input().split())
# target = input()
# mg = []
# for _ in range(m):
#     mg.append(input())
# res = 0
# for i in range(m):
#     count = 0
#     temp = 0
#     while count < n:
#         if mg[i] in target[count:]:
#             count+=target[count:].index(mg[i])+len(mg[i])
#             temp+=1
#         else:
#             break
#     res+=temp
# print(res)

s="owowowo"
ms="owo"
count=0
res={}
for index,i in enumerate(s):
    res[i]=res.get(i,[])+[index]
for i in res[ms[0]]:
        if s[i:i+len(ms)]==ms:
            count+=1
print(count)

