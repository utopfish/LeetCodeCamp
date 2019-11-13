#@Time:2019/11/13 15:02
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:myAtoi.py

class Solution:
    '''
    43.82% 56ms
    '''
    def myAtoi(self, str: str) -> int:
        str=str.lstrip()
        if len(str)==0:
            return 0
        #设置默认输出为0
        last=0
        #如果有符号设置起始位置2，其余的为1
        i=2 if str[0]=='-'or str[0]=='+'  else 1
        #循环，直到无法强转成int，跳出循环
        while i <= len(str):
            try:
                last=int(str[:i])
                i+=1
            except:
                break
        #如果数字超出范围，返回范围最大值
        if last<-2147483648 :
            return -2147483648
        if last>2147483647:
            return 2147483647
        return last