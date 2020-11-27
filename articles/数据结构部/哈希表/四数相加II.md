## 每日一题 - 四数相加 II
### 信息卡片 

- 时间： 2020-11-27
- 题目链接：https://leetcode-cn.com/problems/4sum-ii/
- tag：hash
- 题目描述：

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 $-2^28$ 到 $2^28$ - 1 之间，最终结果不会超过 $2^31$ - 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


### 参考答案
使用hash存两数之和，能把时间复杂度降到$O(n^2)$

```java
class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        int len = A.length;

        int count = 0;
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int i=0;i<len;i++){
            for (int j=0;j<len;j++){
                int sumAB=A[i]+B[j];
                if (map.containsKey(sumAB)) map.put(sumAB,map.get(sumAB)+1);
                else map.put(sumAB,1);
            }
        }
        for (int i=0;i<len;i++){
            for (int j=0;j<len;j++){
                int sumCD=C[i]+D[j];
                if (map.containsKey(-sumCD)) count+=map.get(-sumCD);
            }
        }
        return count;
    }
}
```

### 扩展

### 其他优秀解答 





