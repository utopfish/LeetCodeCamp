# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:huawei_m_02.py
#@time: 2020/9/16 11:07
nums=[2,1,3,4,100]
m=4
nums.sort()
global res
res=float('inf')
def  find(path,index,deep):
    for i in range(index+1,len(nums)):
        if deep==m-1:
            temp=0
            for n in path:
                temp+=(nums[i]-n)
            global res
            res=min(temp,res)
        else:
            find(path+[nums[i]],i,deep+1)

for i in range(len(nums)):
    find([nums[i]],i,1)

print(res)

