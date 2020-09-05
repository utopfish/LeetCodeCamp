#@Time:2020/9/5 11:12
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:bytedance_android01.py
__author__ = "liuAmon"

"""
为了不断优化推荐效果，今日头条每天要存储和处理海量数据。假设有这样一种场景：
我们对用户按照它们的注册时间先后来标号，对于一类文章，每个用户都有不同的喜好值，
我们会想知道某一段时间内注册的用户（标号相连的一批用户）中，有多少用户对这类文章喜好值为k。因为一些特殊的原因，
不会出现一个查询的用户区间完全覆盖另一个查询的用户区间(不存在L1<=L2<=R2<=R1)。
输入：
5
1 2 3 3 5
3
1 2 1
2 4 5
3 5 3
输出：
1
0
2
说明：
样例解释:
有5个用户，喜好值为分别为1、2、3、3、5，
第一组询问对于标号[1,2]的用户喜好值为1的用户的个数是1
第二组询问对于标号[2,4]的用户喜好值为5的用户的个数是0
第三组询问对于标号[3,5]的用户喜好值为3的用户的个数是2
"""

"""


对所用用户，创建map<int 喜爱值，List 喜爱值对应的所有用户升序编号>   O(n）
对于查询的区间编号 [L，R]，在map中查找 喜爱值K，K 对应的用户编号list的区间和 区间[l,r]  
有重合部分，计算出区间重合部分用户数即可。 
"""
n = int(input().strip())
like = [int(x) for x in input().strip().split()]
hashmap = {}
for i in range(n):
    if like[i] not in hashmap:
        hashmap[like[i]] = [i + 1]
    else:
        hashmap[like[i]].append(i + 1)
q = int(input().strip())

for _ in range(q):
    a, b, k = map(int, input().strip().split())
    count = 0
    if k in hashmap:
        for x in hashmap[k]:
            if x >= a and x <= b:
                count += 1
    print(count)