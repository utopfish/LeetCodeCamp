#@Time:2020/9/2 11:04
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:huawei_test02.py
__author__ = "liuAmon"

s=input().replace(" ","")
temp={}
for i in s:
    if i not in temp.keys():
        temp[i]=i
print("".join(temp.keys()))