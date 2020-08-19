#@Time:2020/8/19 14:14
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:huawei01.py
__author__ = "liuAmon"

nums=[]
num=int(input())
while(num!=0):
    nums.append(num)
    num=int(input())

for i in nums:
    print(i//2)