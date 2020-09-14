#@Time:2020/9/14 10:35
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:kmp.py
__author__ = "liuAmon"
def get_next(p):
    n=len(p)
    nex=[0]*(n+1)
    nex[0]=-1
    i,j=0,-1
    while i<n:
        if j==-1 or p[i]==p[j]:
            i+=1
            j+=1
            nex[i]=j
        else:
            j=nex[j]
    return nex
def KMP(t,p):
    nex=get_next(p)
    i,j=0,-1
    while i<len(t) and j<len(p):
        if j==-1 or t[i]==p[j]:
            i+=1
            j+=1
        else:
            j=nex[j]
    if j==len(p):
        return True
    return False

if __name__=="__main__":
    target="BBC ABCDAB ABCDABCDABDE"
    pattern="ABCDABD"
    print(KMP(target,pattern))
