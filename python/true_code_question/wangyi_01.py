# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:wangyi_01.py
#@time: 2020/9/27 19:05

"""
1
7 3
0 2
2 0
4 4

"""
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    res=[]
    for _ in range(m):
        res.append(list(map(int,input().split())))
    matrix=[[0]*n for _ in range(n)]
    left,right,top,bottom=0,n-1,0,n-1
    count=1
    flag=0
    while left<=right and top<=bottom:
        if flag%2==0:
            for column in range(left, right + 1):
                matrix[top][column]=count
                count+=1
            for row in range(top + 1, bottom + 1):
                matrix[row][right]=count
                count+=1
            for column in range(right - 1, left, -1):
                matrix[bottom][column]=count
                count+=1
            for row in range(bottom, top, -1):
                matrix[row][left]=count
                count+=1
        else:
            for row in range(top,bottom):
                matrix[row][left]=count
                count+=1
            for column in range(left, right ):
                matrix[bottom][column]=count
                count+=1
            for row in range(bottom, top-1, -1):
                matrix[row][right] = count
                count += 1
            for column in range(right - 1, left, -1):
                matrix[top][column] = count
                count += 1
        flag += 1
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

    for i in res:
        print(matrix[i[0]][i[1]])




