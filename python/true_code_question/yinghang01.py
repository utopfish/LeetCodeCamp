#@Time:2020/9/6 14:50
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:yinghang01.py
__author__ = "liuAmon"

"""
输入：
5
0 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 0 0 1 0 1 1 0 0
4
输出:
4->1->3->4
4->2->0->1->3->4
"""
n=int(input())
temp=list(map(int,input().split(" ")))
nums=[]
for i in range(n):
    nums.append(temp[i*n:(i+1)*n])

begin=int(input())
queue=[begin]
id=queue[0]

def BFSTravel(v,path):
    q=[]
    for index,i in enumerate(nums[v]):
        if i == 1:
            q.append((index,path+str(index)))
    while q!=[]:
        e=q.pop(0)
        for index,i in enumerate(nums[e[0]]):
            if i == 1:
                s=e[1][1:]
                if str(v) ==str(index):
                    print(e[1])
                elif str(index) not in e[1]:
                    q.append((index,e[1]+str(index)))
BFSTravel(begin,str(begin))
















