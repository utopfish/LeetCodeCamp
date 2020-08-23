#@Time:2020/8/23 17:04
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:isHappy.py
__author__ = "liuAmon"

"""
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，
那么这个数就是快乐数。


"""
def isHappy(self, n: int) -> bool:
    def getNext(n):
        sum_num = 0
        while (n > 0):
            n, digit = divmod(n, 10)
            sum_num += digit ** 2
        return sum_num

    s = set()
    while n != 1 and n not in s:
        s.add(n)
        n = getNext(n)
    return n == 1