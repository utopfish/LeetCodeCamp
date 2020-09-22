#@Time:2020/9/21 20:21
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:银行.py
__author__ = "liuAmon"

"""
描述：
给定一个非负数，计算其二进制中1的数目，并按数组返回
输入：
2
输出：
[0,1,1]

"""

n=int(input())
res=[]
for i in range(n+1):
    temp=0
    while i:
        temp+=i&1
        i>>=1
    res.append(temp)
print(res)