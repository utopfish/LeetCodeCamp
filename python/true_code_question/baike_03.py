# -*- coding: utf-8 -*-
"""
@Project :  PyCharm
@File    : baike_03.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/10/26 
"""

"""
1
1 1000
"""
# t=int(input())
# for _ in range(t):
#     l,r=map(int,input().split())
#     count=0
#     for i in range(l,r+1):
#         max_n=0
#         min_n=9
#         while i:
#             max_n=max(max_n,i%10)
#             min_n=min(min_n,i%10)
#             i//=10
#         if min_n*2>=max_n:
#             count+=1
#     print(count)


t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    count = 0
    while l <= r:
        max_n = 0
        max_ind = 0
        min_n = 9
        min_ind = 0
        ind = 0
        i=l
        while i:
            tmp = i % 10
            if max_n < tmp:
                max_n = tmp
                max_ind = ind
            if min_n > tmp:
                min_n = tmp
                min_ind = ind
            ind += 1
            i//= 10
        res_ind = min(min_ind, max_ind)
        if min_n * 2 >= max_n:
            if min_n==0 and max_n==9:
                count += 10 ** res_ind
                l += 10 ** res_ind
            else:
                count += 1
                l += 1
        else:
            l+=1
    print(count)