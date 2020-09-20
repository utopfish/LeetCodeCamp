# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:bytedance_01.py
#@time: 2020/9/20 20:34
s="ab"*10000099
import time
# start=time.time()
# flag=0
# for i in range(1,len(s)//2):
#     if s==(s+s)[i:len(s)+i]:
#         flag=1
#         print(s[:i])
#         break
# if flag==0:
#     print(s)
# print("耗时:{}".format(str(time.time()-start)))

sss=time.time()
i, start, end, length = 1, 0, 1, len(s)
while i < length:
    if s[i] != s[start]:
        end = i + 1
        i += 1
    else:
        tmp = i + end - start
        if tmp <= length:
            if s[start:end] == s[i:tmp]:
                i = tmp
                continue
            else:
                end = tmp
                i = end
        else:
            end = length
            break

if end - start < length:
    print(''.join(s[start:end]))
else:k
    print(s)

print("耗时:{}".format(str(time.time()-sss)))