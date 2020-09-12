# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:wangyi04.py
#@time: 2020/9/12 15:55

"""
0 1 2
3 4 5
6
0 4
0 3
1 3
1 4
2 5
2 4
"""
import sys
MAX_INT=sys.maxsize
boys=list(map(int,input().split()))
girls=list(map(int,input().split()))
n=int(input())
nums=[]
for _ in range(n):
    nums.append(list(map(int,input().split())))
rela=[[0]*len(boys+girls) for _ in range(len(boys+girls))]
for num in nums:
    rela[num[0]][num[1]]=1
count=0
b_temp=[sum(i) for i in rela[:len(boys)]]
b_temp=[MAX_INT if i ==0 else i for i in b_temp]
min_boy=min(b_temp)

g_temp=[sum(i) for i in rela[len(boys):len(boys)+len(girls)]]
g_temp=[MAX_INT if i ==0 else i for i in g_temp]
min_girl=min(g_temp)


while min(min_boy,min_girl)!=MAX_INT:
    count+=1
    if min_girl<min_boy:
        girl_loc=g_temp.index(min_girl)+len(boys)
        boy_loc=rela[:][girl_loc].index(1)
        rela[boy_loc][girl_loc] = 0
    else:
        boy_loc=b_temp.index(min_boy)
        girl_loc=rela[boy_loc].index(1)
        rela[boy_loc][girl_loc]=0

    b_temp = [sum(i) for i in rela[:len(boys)]]
    b_temp = [MAX_INT if i == 0 else i for i in b_temp]
    min_boy = min(b_temp)
    g_temp = [sum(i) for i in rela[len(boys):len(boys) + len(girls)]]
    g_temp = [MAX_INT if i == 0 else i for i in g_temp]
    min_girl = min(g_temp)

print(count)



