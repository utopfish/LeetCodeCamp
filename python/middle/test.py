#@Time:2020/8/19 19:41
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:test.py
__author__ = "liuAmon"

import sys
if __name__=="__main__":
    n = int(sys.stdin.readline().strip())
    nums=[]
    for i in range(n):
        nums.append(list(map(int,input().strip().split(" "))))
    temp11={}
    temp21={}
    for i in range(n):
        if nums[i][1]==1:
            temp11[nums[i][0]]=i+1
        else:
            temp21[nums[i][0]]=i+1
    temp1=sorted(temp11.items(),key=lambda x:x[0])
    temp2=sorted(temp21.items(),key=lambda x:x[0])
    sum1=[i[0] for i in temp1[-3:]]
    sum2=[i[0] for i in temp2[-3:]]
    if len(temp2)<3 or sum(sum1)>sum(sum2):
        res=[ str(temp11.get(i)) for i in sum1]
        print(" ".join(res))
        print("1")
        print(sum(sum1))
    elif len(temp1)<3 or sum(sum1)<sum(sum2):
        res=[ str(temp21.get(i)) for i in sum2]
        print(" ".join(res))
        print("2")
        print(sum(sum2))
    else:
        print('null')

