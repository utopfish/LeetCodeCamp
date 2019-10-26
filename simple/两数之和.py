# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:两数之和.py
#@time: 2019/10/26 11:20
import unittest

class twoSumTestCase(unittest.TestCase):
    def test_twoSum1(self):
        result=Solution1.twoSum([2, 7, 11, 15],9)
        self.assertEqual(result,[0, 1])
    def test_twoSum2(self):
        result=Solution2.twoSum([2, 7, 11, 15],9)
        self.assertEqual(result, [1,0])
class Solution1:
    '''
    参考了大神们的解法，通过哈希来求解，这里通过字典来模拟哈希查询的过程。
    通过字典的方法，查找效率快很多，执行速度大幅缩短，共 88ms。
    '''
    def twoSum(nums, target):
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
class Solution2:
    '''
    不需要 mun2 不需要在整个 dict 中去查找。可以在 num1 之前的 dict 中查找，因此就只需要一次循环可解决。
    运行速度在 70ms 多。
    '''
    def twoSum(nums, target):
        hashmap={}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i,hashmap.get(target - num)]
            hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


if __name__=="__main__":
    unittest.main()


