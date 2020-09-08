#@Time:2020/9/8 19:13
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:xiaomi04.py
__author__ = "liuAmon"

n=int(input())
while n!=0:
    s=[]
    for _ in range(n):
        s.append(input())
    encoded=input()[:-1].split()