# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:huawei_m_01.py
#@time: 2020/9/16 10:13
n,m=3,3
global count
count=0
dd=[(1,0),(0,1)]
def find(x,y,end):
    for i in dd:
        new_x,new_y=x+i[0],y+i[1]
        if new_x<n and new_y<m:
            if [new_x,new_y]==end:
                global count
                count+=1
                return
            else:
                find(new_x,new_y,end)
find(0,0,[2,2])
print(count)
