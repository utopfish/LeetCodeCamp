# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:meituan_02.py
#@time: 2020/9/20 10:21
n,m,p,q=map(int,input().split())
road=[]
for i in range(n):
    road.append(input())
    if 'S' in road[i]:
        cur=[i,road[i].index('S')]
path=input()
score=0

dd=[[1,0],[-1,0],[0,1],[0,-1]]

visited=[[False]*m for _ in range(n)]
visited[cur[0]][cur[1]]=True
for i in range(len(path)):
    if path[i]=='S':
        nex_x=cur[0]+dd[0][0]
        nex_y=cur[1]+dd[0][1]
    elif path[i]=='W':
        nex_x = cur[0] + dd[1][0]
        nex_y = cur[1] + dd[1][1]
    elif path[i]=='A':
        nex_x=cur[0]+dd[3][0]
        nex_y=cur[1]+dd[3][1]
    elif path[i]=='D':
        nex_x = cur[0] + dd[2][0]
        nex_y = cur[1] + dd[2][1]
    if 0<=nex_x<n and 0<=nex_y<m and road[nex_x][nex_y]!='#'  :
        if road[nex_x][nex_y]=="O" and visited[nex_x][nex_y]==False:
            score+=p
        elif road[nex_x][nex_y]=="X" and visited[nex_x][nex_y]==False:
            score-=q
        cur[0]=nex_x
        cur[1]=nex_y
        visited[nex_x][nex_y]=True
print(score)
