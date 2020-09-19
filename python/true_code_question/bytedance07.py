#@Time:2020/9/19 17:19
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:bytedance07.py
__author__ = "liuAmon"

n=int(input())
tower=list(map(int,input().split()))
begin=0
cur_life=0
for i in range(n):
    cur_life=cur_life+cur_life-tower[i] if cur_life>tower[i] else cur_life-(tower[i]-cur_life)
    while cur_life<0:
        begin+=1
        cur_life=begin
        for j in range(i+1):
            cur_life=cur_life+cur_life-tower[j] if cur_life>tower[j] else cur_life-(tower[j]-cur_life)
print(begin)