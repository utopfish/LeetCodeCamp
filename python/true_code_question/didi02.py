#@Time:2020/9/14 11:21
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:didi02.py
__author__ = "liuAmon"

#Floyd算法求最短路径
"""
输入：
4 4
1 2 5
1 3 5
2 4 8
3 4 6
1 2 7.9/8 
"""
def shortest_path(n,nums):
    path=[[float('inf')]*n for _ in range(n)]
    for num in nums:
        path[num[0]-1][num[1]-1]=num[2]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                path[i][j]=min(path[i][k]+path[k][j],path[i][j])
    return path
if __name__=="__main__":
    n=4
    # nums=[[1,2,5],
    #       [1,3,5],
    #       [2,4,8],
    #       [3,4,6]]
    nums=[[1,2,25],
          [1,3,18],
          [2,4,28],
          [3,4,22],]
    d=shortest_path(n,nums)
    print(d[0][3])
