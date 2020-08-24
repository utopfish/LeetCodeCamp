#@Time:2020/8/24 18:34
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:xiaohongshu03.py
__author__ = "liuAmon"

"""
在游戏中，击败魔物后，薯队长获得了N件宝物，接下来得把这些宝物卖给宝物回收员来赚点小钱。
这个回收员有个坏毛病，每次卖给他一件宝 物后，之后他就看不上比这件宝物差的宝物了。
在这个世界中，衡量宝物的好坏有两个维度，稀有度X和实用度H，回收员在回收一个宝物A 
后，下一个宝物的稀有度和实用度都不能低于宝物A。那么薯队长如何制定售卖顺序，
才能卖给回收员宝物总个数最多。 
输入：
4
3 2
1 1 
1 3
1 2
输出：
3
"""

import sys





N = int(input())
z_list = []
for i in range(N):
    x, h = map(int, sys.stdin.readline().strip().split())
    z_list.append([x, h])

z_list.sort(key=lambda x:(x[0],x[1]))
arr = [item[1] for item in z_list]


def binary_search(arr1, start, end, target):
    if start < end:
        mid = (start + end) // 2
        if arr1[mid] < target:  # 去找大于等于的位置
            return binary_search(arr1, mid + 1, end, target)
        else:
            return binary_search(arr1, start, mid, target)
    else:
        return start


len_list = [arr[0]]
for index in range(1, len(arr)):
    item = arr[index]
    pos = binary_search(arr1=len_list, start=0, end=len(len_list), target=item)

    if len(len_list) == pos:
        len_list.append(item)
    else:
        len_list[pos] = item
print(len(len_list))