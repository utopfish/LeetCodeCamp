#@Time:2020/8/24 17:22
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:xiaohongshu01.py
__author__ = "liuAmon"
"""
 薯队长写了一篇笔记草稿，请你帮忙输出最后内容。
1.输入字符包括，"("    ,    ")"    和    "<"和其他字符。 
2.其他字符表示笔记内容。
3.()之间表示注释内容，任何字符都无效。    括号保证成对出现。
4."<"表示退格,    删去前面一个笔记内容字符。括号不受"<"影响    。  

输入：
Corona(Trump)USA<<<Virus
输出：
CoronaVirus
"""
string=input().strip()
def subSt(string):
    flag=0
    begin=0
    end=0
    for index,s in enumerate(string):
        if s=='(':
            flag+=1
            if flag==1:
                begin=index
        elif s==')':
            flag-=1
            if flag==0:
                end=index
                break
    return string[:begin]+string[end+1:]
def subSt2(s):
    for i in range(len(s)-1):
        if s[i+1]=='<':
            return s[:i]+s[i+2:]
while '(' in string:
    string=subSt(string)
while '<' in string:
    string=subSt2(string)
print(string)