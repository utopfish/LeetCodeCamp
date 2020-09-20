#@Time:2020/9/19 16:27
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:bytedance04.py
__author__ = "liuAmon"

t=int(input())

for _ in range(t):
    max_num = 1
    p=int(input())
    hash={}
    for i in range(p):
        temp=list(map(int,input().split()))[1:]
        for t in range(len(temp)//2):
            mark="|".join(map(str,temp[t*2:t*2+2]))
            hash[mark]=hash.get(mark,[])+[i]
    for i in hash.keys():
        count=1
        for num in range(1,len(hash[i])):
            if hash[i][num]-hash[i][num-1]==1:
                count+=1
                max_num = max(max_num, count)
            else:
                count=1
    print(max_num)



