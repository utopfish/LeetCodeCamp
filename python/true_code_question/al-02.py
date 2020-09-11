# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:al-02.py
#@time: 2020/9/11 9:42
"""

5 4
0 8 -1 0
0 0 8 0
0 8 8 0
0 8 0 -1
0 -1 -1 0
"""
n,m=map(int,input().split())
res=[]
for i in range(n):
    res.append(list(map(int,input().split())))
# 0,wu 1,up 2 dowm 3 left 4right
def dsf(loc,mark):
    temp=[]
    locs.append(loc)
    if loc[0]-1>=0 and mark!=2:
        if res[loc[0]-1][loc[1]]!=-1:
            temp.append(res[loc[0]-1][loc[1]])
        else:
            temp+=dsf([loc[0]-1,loc[1]],1)
    if loc[0]+1<n and mark!=1:
        if res[loc[0]+1][loc[1]]!=-1:
            temp.append(res[loc[0]+1][loc[1]])
        else:
            temp+=dsf([loc[0]+1,loc[1]],2)
    if loc[1]-1>=0 and mark!=4:
        if res[loc[0]][loc[1]-1]!=-1:
            temp.append(res[loc[0]][loc[1]-1])
        else:
            temp+=dsf([loc[0],loc[1]-1],3)
    if loc[1]+1<m and mark!=3:
        if res[loc[0]][loc[1]+1]!=-1:
            temp.append(res[loc[0]][loc[1]+1])
        else:
            temp+=dsf([loc[0],loc[1]+1],4)
    return temp
for i in range(n):
    for j in range(m):
        if res[i][j]==-1:
            locs=[]
            sum_num=dsf([i,j],0)
            for l in locs:
                res[l[0]][l[1]]=sum(sum_num)//len(sum_num)
for i in range(n):
    temp=[str(j) for j in res[i]]
    print(" ".join(temp))