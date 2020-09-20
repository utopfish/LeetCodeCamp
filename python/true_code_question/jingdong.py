#@Time:2020/9/17 19:39
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:jingdong.py
__author__ = "liuAmon"

"""
2
2 2
. E
S .
2 2
# E
S #
"""
dd=[[-1,0],[1,0],[0,-1],[0,1]]
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    road=[]
    for i in range(n):
        road.append(input().split())
        if 'S' in road[i]:
            wz=[i,road[i].index('S')]
        if 'E' in road[i]:
            gz=[i,road[i].index('E')]
    def find(start, path):
        res=[]
        for d in dd:
            new_x = start[0] + d[0]
            new_y = start[1] + d[1]
            if 0 <= new_x < n and 0 <= new_y < m and road[new_x][new_y]!='#'and path[new_x][new_y]==-1:
                path[new_x][new_y]=path[start[0]][start[1]]+1
                res.append([new_x,new_y])
        return res
    path=[[-1]*m for _ in range(n)]
    q=[wz]
    while q:
        cur_node=[]
        for i in q:
            res=find(i,path)
            cur_node+=res
        q=cur_node
    if path[gz[0]][gz[1]]==-1:
        print("NO")
    else:
        print("YES")






