# -*- coding: utf-8 -*-
"""
@Project :  PyCharm
@File    : LCP5601.py
@Author  : Mr.Liu Meng
@E-mail  : utopfish@163.com
@Time    : 2020/11/15 
"""

from typing import List
class OrderedStream:

    def __init__(self, n: int):
        self.stream = [0] * (n + 1)
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id]=value
        if self.ptr == id:
            ret = []
            while self.ptr<len(self.stream) and self.stream[self.ptr] != 0:
                ret.append(self.stream[self.ptr])
                self.ptr += 1
            return ret
        else:
            return []

if __name__=="__main__":
    os = OrderedStream(5);
    os.insert(3, "ccccc"); #插入(3, "ccccc")，返回[]
    os.insert(1, "aaaaa"); # 插入(1, "aaaaa")，返回["aaaaa"]
    os.insert(2, "bbbbb"); # 插入(2, "bbbbb")，返回["bbbbb", "ccccc"]
    os.insert(5, "eeeee"); # 插入(5, "eeeee")，返回[]
    os.insert(4, "ddddd"); # 插入(4, "ddddd")，返回["ddddd", "eeeee"]