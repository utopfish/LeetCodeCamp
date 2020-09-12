# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:vivo01.py
#@time: 2020/9/12 19:51

"""
最短路径，15 为矩阵大小，0 7 7 7 分别为起点终点，输出最短路径，@,#不能通行
15
0 7 7 7
*5#++B+B+++++$3
55#+++++++###$$
###$++++++#+*#+
++$@$+++$$$3+#+
+++$$+++$+4###+
A++++###$@+$++A
+++++#++$#$$+++
A++++#+5+#+++++
+++$$#$++#++++A
+++$+@$###+++++
+###4+$+++$$+++
+#+3$$$+++$##++
+#*+#++++++#$$+
$####+++++++$##
3$+++B++B++++#5
"""


n=int(input())
point=list(map(int,input().split()))
maze=[]
import sys
for i in range(n):
    maze.append(input())
# dp=[[0]*n for _ in range(n)]
# temp=0
# for i in range(point[0],point[2]+1):
#     for j in range(point[1],point[3]+1):
#         t=m[i][j]
#         if i>= point[0] and m[i][j] not in ['@','#']:
#             dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
#             temp+=1
#         elif m[i][j] in ['@','#']:
#             dp[i][j]=min(dp[i-1][j],dp[i][j-1])+3
#             temp+=3
#
#
# print(temp)

dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
from queue import Queue
# 计算（x, y）到maze中其他点的距离，结果保存在ret中
def bfs(x, y,  n):
    ret = [[-1]*n for _ in range(n)]
    ret[x][y] = 0
    q = Queue()
    q.put((x,y))
    while q.qsize():
        curx, cury = q.get()
        for dx, dy in dd:
            nx = curx + dx
            ny = cury + dy
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] not in  ['#','@'] and ret[nx][ny] == -1:
                ret[nx][ny] = ret[curx][cury] + 1
                q.put((nx, ny))
    return ret

res=bfs(point[0],point[1],n)
print(res[point[2]][point[3]])

