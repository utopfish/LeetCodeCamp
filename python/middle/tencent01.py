#@Time:2020/8/19 14:31
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:tencent01.py
__author__ = "liuAmon"

st=input()
def rev(string):
    while '|' in string:
        if '[' in string:
            mark=0
            left = string.find('[')
            for index,i in enumerate(string[left+1:]):
                if i=='[':
                    mark+=1
                elif mark==0 and i==']':
                    right=index+left+1
                elif i==']':
                    mark-=1
            tem=string[left:right+1]
            string=string.replace(string[left:right+1],rev(string[left+1:right]))
        elif '|' in string:
            temp=string.split('|')
            s=''
            for _ in range(int(temp[0])):
                s+=temp[1]
            return s
    return string
st=rev(st)
print(st)