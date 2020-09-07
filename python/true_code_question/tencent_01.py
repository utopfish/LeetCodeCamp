#@Time:2020/9/6 13:39
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:tencent_01.py
__author__ = "liuAmon"

s = input()


def rev(s):
    while '[' in s:
        for i in range(len(s)):
            mark = 0
            if s[i] == '[':
                if mark==0:
                    begin = i
                mark += 1
            elif  s[i] == ']':
                if mark==0:
                    end = i
                    break
                mark -= 1
        s = s[:begin]+rev(s[begin + 1: end])+s[end+1:]

    if '|' in s:
        temp = s.split("|")
        k = ''
        for _ in range(int(temp[0])):
            k += temp[1]
        return k
    else:
        return s


print(rev(s))