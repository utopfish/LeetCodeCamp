#@Time:2020/9/21 15:55
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:最小循环子串.py
__author__ = "liuAmon"
"""
三种方法应该都能解决问题，这个需要好好整理一下

"""
s="aba"*1000000+"C1"
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
    if len(s)%i==0 and s[:i]==s[-i:] and s[i:]==s[:-i]:
        flag=1
        print(s[:i])
        break
if flag==0:
    print(s)
print("耗时:{}".format(str(time.time()-start)))

start=time.time()
n=len(s)
t=0
for i in range(1,n):
    if n%i==0:
        flag=0
        for j in range(i,n):
            if s[j]!=s[j%i]:
                flag=1
                break
        if flag==0:
            print(s[:i])
            t=1
            break
if t==0:
    print(s)
print("耗时:{}".format(str(time.time()-start)))


