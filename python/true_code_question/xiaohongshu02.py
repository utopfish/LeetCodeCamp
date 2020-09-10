#@Time:2020/8/24 17:51
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:xiaohongshu02.py
__author__ = "liuAmon"
"""
薯队长写了n篇笔记，编号从1~n,每篇笔记都获得了不少点赞数。    
薯队长想从中选出一些笔记，作一个精选集合。挑选的时候有两个规则：
1.不能出现连续编号的笔记。 
2.总点赞总数最多 
如果满足1，2条件有多种方案，挑选笔记总数最少的那种 

输入：
4
1 2 3 1
输出：
4 2
"""
n=int(input())
nums=list(map(int,input().strip().split(" ")))
dp = [0 for _ in range(n+2)]
dpNum = [0 for _ in range(n+2)]

for i in range(2,n+2):
    if dp[i-1]<dp[i-2]+nums[i-2]:
        dp[i]=dp[i-2]+nums[i-2]
        dpNum[i]=dpNum[i-2]+1
    else:
        dp[i]=dp[i-1]
        dpNum[i]=dpNum[i-1]
print(dp[n+1], dpNum[n+1])