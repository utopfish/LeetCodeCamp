#@Time:2020/9/19 15:46
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:bytedance02.py
__author__ = "liuAmon"
"""
输入：
4 3
1 2 3 4
输出：
4
说明：
可选方案 (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)
"""
n, dist = map(int, input().split())
nums = list(map(int, input().split()))
res = 0
left = 0
right = 2

while left < n - 2:
    while right < n and nums[right] - nums[left] <= dist:
        right += 1
    if right - 1 - left >= 2:
        num = right - left - 1
        res += num * (num - 1) // 2
    left += 1

print(res % 99997867)
