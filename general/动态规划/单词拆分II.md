## 每日一题 - 单词拆分 II
### 信息卡片 

- 时间： 2020-11-01
- 题目链接：https://leetcode-cn.com/problems/word-break-ii/
- tag：dp 
- 题目描述：

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

    分隔时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。

示例 1：

输入:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    输出:
    [
    "cats and dog",
    "cat sand dog"
    ]

示例 2：

    输入:
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    输出:
    [
    "pine apple pen apple",
    "pineapple pen apple",
    "pine applepen apple"
    ]
    解释: 注意你可以重复使用字典中的单词。

示例 3：

    输入:
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出:
    []

### 前置题目 [[单词拆分]]

### 参考答案

#倒叙查找剪枝问题
动态规划,先使用前置题中的方法找到能进行划分的点
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        #转为set 加速查询
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        # 大佬说倒序查找在这里能进行一些剪枝
        for right in range(1, n + 1):
            for left in range(right - 1, -1, -1):
                if (dp[left] and (s[left:right] in wordDict)):
                    dp[right] = True
                    # break能节省一点计算，不太懂，现在正序遍历其实差别不大，就暂时这样吧。
                    break

        def dfs(begin, path):
            if begin == n:
                res.append(" ".join(path))
                return
            for i in range(begin+1, n+1):
                if dp[i] and s[begin:i] in wordDict:
                    path.append(s[begin:i])
                    dfs(i, path)
                    # 之前这里使用path.remove(string[begin:i])报错，是因为存在相同的元素，导致删除错误
                    path.pop(-1)

        if dp[-1]:
            dfs(0, [])
        return res

```
使用动态规划的优化，只记录能进行划分节点的位置，省掉了一些遍历，效果提升不如在单词拆分题中明显。
```python
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        #转为set 加速查询
        wordDict = set(wordDict)
        n = len(s)
        trues = [0]
        # 对能进行划分的其实位置进行单独存储，减小了时间和空间复杂度。与法二思想类似。
        for j in range(0, len(s) + 1):
            for i in trues:
                if s[i:j] in wordDict:
                    trues.append(j)
                    break

        def dfs(begin, path):
            if begin == n:
                res.append(" ".join(path))
                return
            for i in trues:
                if  s[begin:i] in wordDict:
                    path.append(s[begin:i])
                    dfs(i, path)
                    # 之前这里使用path.remove(string[begin:i])报错，是因为存在相同的元素，导致删除错误
                    path.pop(-1)
        if trues[-1]==n:
            dfs(0, [])
        return res
```

### 扩展

### 其他优秀解答 





