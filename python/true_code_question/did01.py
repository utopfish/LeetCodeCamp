#@Time:2020/8/19 19:24
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:did01.py
__author__ = "liuAmon"
#一个数组有 N 个元素，求连续子数组的最大和。 例如：[-1,2,1]，和最大的连续子数组为[2,1]，其和为 3
times=int(input())
try:
    nums=[int(i) for i in input().split(" ")]
except:
    pass
head=0
tail=0
ma=0
while (head<len(nums)):
    if sum(nums[head:tail+1])>ma:
        ma=sum(nums)
        tail+=1
    else:
        head+=1
