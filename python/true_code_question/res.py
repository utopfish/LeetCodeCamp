# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:res.py
#@time: 2020/9/6 12:08

"""
135682318
23457
14282123
14231728
3
1724153
"""



import re
s=input()
string=[s]
while len(s)>1:
    s=input()
    string.append(s)
num=int(string[-1])
del string[-1]
taget=input()
taget=re.sub( '[{}-9]'.format(num),"", taget)
temp=[]
for i in string:
    t=re.sub('[{}-9]'.format(num),"", i)
    temp.append(t)
for i in range(len(string)):
    if temp[i].find(taget)>=0:
        print(string[i])






