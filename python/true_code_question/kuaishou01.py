#@Time:2020/9/7 10:56
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:kuaishou01.py
__author__ = "liuAmon"

n=int(input())
nums=list(map(int,input().split()))
min_sum=int(1e9)
nums.sort()
i,j=0,len(nums)
while i<j:
    med=(i+j-1)//2
    left=sum(nums[:med])
    right=sum(nums[med:])
    if min_sum>abs(left-right):
            min_sum=abs(left-right)
    if left>right:
        j=med-1
    else:
        i=med+1
print(min_sum)