# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:singleNumber.py
#@time: 2019/11/8 15:45
class Solution4(object):
    '''
    方法 4：位操作
概念
    如果我们对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位
        a⊕0=a
    如果我们对相同的二进制位做 XOR 运算，返回的结果是 0
        a⊕a=0
    XOR 满足交换律和结合律
        a⊕b⊕a=(a⊕a)⊕b=0⊕b=ba
    '''
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()


