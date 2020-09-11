#@Time:2020/8/19 16:21
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:huawei02.py
__author__ = "liuAmon"

times=int(input())
buildings=[int(i) for i in input().split(" ")]
looking=[1 for _ in range(len(buildings))]
for i in range(len(buildings)):
    mar=0
    mal=0
    for j in range(i-1,-1,-1):
        if mal<buildings[j]:
            looking[i]+=1
            mal=buildings[j]
    for j in range(i+1,len(buildings)):
        if mar<buildings[j]:
            looking[i]+=1
            mar=buildings[j]
looking=[str(i) for i in looking]
print(" ".join(looking))