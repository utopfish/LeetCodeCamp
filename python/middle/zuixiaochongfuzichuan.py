# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:zuixiaochongfuzichuan.py
#@time: 2020/9/20 23:02
# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:bytedance_01.py
#@time: 2020/9/20 20:34

"""
解决最小重复子串的几种方法，最好的s+s[i:len(s)+i]
在s长度为10^8的情况下测试超时了，之后找找可能python的问题还是能找到更好的办法
"""
s="aba"*2
import time

start=time.time()
def get_next(p):
    n=len(p)
    nex=[0]*(n)
    nex[0]=0
    i,j=0,0
    for i in range(1,n):
        while j and s[i]!=s[j]:
            j=nex[j-1]
        if s[i]==s[j]:
            j+=1
        nex[i]=j
    return nex
l=len(s)
next=get_next(s)
print(s[:l-next[l-1]])
print("耗时:{}".format(str(time.time()-start)))

start=time.time()
flag=0
for i in range(1,len(s)//2+1):
    if s==(s+s)[i:len(s)+i]:
        flag=1
        print(s[:i])
        break
if flag==0:
    print(s)
print("耗时:{}".format(str(time.time()-start)))

sss=time.time()
i, start, end, length = 1, 0, 1, len(s)
while i < length:
    if s[i] != s[start]:
        i=end = i + 1
    else:
        tmp = i + end - start
        if tmp <= length:
            if s[start:end] == s[i:tmp]:
                i = tmp
                continue
            else:
                i = end = end + 1
        else:
            end = length
            break

if end - start < length:
    print(''.join(s[start:end]))
else:
    print(s)
print("耗时:{}".format(str(time.time()-sss)))
