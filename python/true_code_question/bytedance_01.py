#@Time:2020/9/19 14:59
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:bytedance_01.py
__author__ = "liuAmon"

"""
描述：
输入： 第1行为n代表用户的个数 第2行为n个整数，第i个代表用户标号为i的用户对某类文章的喜好度 第3行为一个正整数q代表查
询的组数  第4行到第（3+q）行，每行包含3个整数l,r,k代表一组查询，即标号为l<=i<=r的用户中对这类文章喜好值为k的用户的
个数。 数据范围n <= 300000,q<=300000 k是整型

输入:
5
1 2 3 3 5
3
1 2 1
2 4 5
3 5 3
输出：
1
0
2
"""

n=int(input())
nums=list(map(int,input().split()))
q_times=int(input())
q=[]
for _ in range(q_times):
    q.append(list(map(int, input().split())))
r={}
for index,i in enumerate(nums):
    r[i]=r.get(i,[])+[index]
for i in q:
    temp=r[i[2]]
    count =0
    for t in temp:
        if t in range(i[0]-1,i[1]):
            count+=1
    print(count)
