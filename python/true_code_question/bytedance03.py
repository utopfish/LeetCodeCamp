#@Time:2020/9/19 17:39
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:bytedance03.py
__author__ = "liuAmon"

"""
雀魂，递归计算
"""
def isHu(nums):
    """
    判断是否可以胡牌
    :param nums:
    :return:
    """
    if not nums:
        return True
    n = len(nums)
    count0 = nums.count(nums[0])
    # 没出现过雀头，且第一个数字出现的次数 >= 2,去掉雀头剩下的能不能和牌
    if n % 3 != 0 and count0 >= 2 and isHu(nums[2:]) == True:
        return True
    # 如果第一个数字出现次数 >= 3，去掉这个刻子后看剩下的能和牌
    if count0 >= 3 and isHu(nums[3:]) == True:
        return True
    # 如果存在顺子，移除顺子后剩下的能和牌
    if nums[0] + 1 in nums and nums[0] + 2 in nums:
        last_nums = nums.copy()
        last_nums.remove(nums[0])
        last_nums.remove(nums[0] + 1)
        last_nums.remove(nums[0] + 2)
        if isHu(last_nums) == True:
            return True
    # 以上条件都不满足，则不能和牌
    return False


def main(nums):
    """
    遍历所有可以抓到的牌看能不能胡牌
    :return:
    """
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    #如果手里已经有了四张某种牌，那就不可能摸到了
    card_list = set(range(1, 10)) - {i for i, v in d.items() if v == 4}
    res = []
    for i in card_list:
        if isHu(sorted(nums + [i])):  # 如果这种抽牌方式可以和牌
            res.append(i)  # 加入和牌类型列表
    res = ' '.join(str(x) for x in sorted(res)) if res else '0'
    print(res)


s = input()
nums = [int(x) for x in s.split()]
main(nums)