#@Time:2020/9/2 16:52
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:firstUniqChar.py
__author__ = "liuAmon"


def firstUniqChar(s: str) -> str:
    res = {}
    temp = {}
    for index,i  in enumerate(s):
        if i not in res.keys() and i not in temp.keys():
            res[i] = index
            temp[i] = i
        elif i in res.keys():
            del res[i]
    if len(res.keys()) == 0:
        return " "
    else:
        s = sorted(res.items(), key=lambda x: x[1])
        return s[0][0]
print(firstUniqChar("abaccdeff"))