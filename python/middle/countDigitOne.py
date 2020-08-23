#@Time:2020/8/23 18:14
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:countDigitOne.py
__author__ = "liuAmon"

"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

"""
def countDigitOne( n: int) -> int:
    dig, res = 1, 0
    high, cur, low = n // 10, n % 10, 0
    while high != 0 or cur != 0:
        if cur == 0:
            res += high * dig
        elif cur == 1:
            res += high * dig + low + 1
        elif cur > 1:
            res += (high + 1) * dig
        low += cur * dig
        cur = high % 10
        high = high // 10
        dig *= 10
    return res
if __name__=="__main__":
    print(countDigitOne(12))