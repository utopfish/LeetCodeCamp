## 每日一题 - Z 字形变换
### 信息卡片 

- 时间： 2020-10-15
- 题目链接：https://leetcode-cn.com/problems/zigzag-conversion/
- tag：字符串
- 题目描述：

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

    L   C   I   R
    E T O E S I I G
    E   D   H   N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

示例 1:

    输入: s = "LEETCODEISHIRING", numRows = 3
    输出: "LCIRETOESIIGEDHN"

示例 2:

    输入: s = "LEETCODEISHIRING", numRows = 4
    输出: "LDREOEIIECIHNTSG"
    解释:

    L     D     R  
    E   O E   I I 
    E C   I H   N
    T     S     G




### 参考答案


```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2:
            return s
        tmp=["" for _ in range(numRows) ]
        i,flag=0,-1
        for c in s:
            tmp[i]=tmp[i]+c
            if i==0 or i==numRows-1: flag=-flag
            i+=flag
        return "".join(tmp)

```

```java
class Solution {
    public String convert(String s, int numRows) {
        if (numRows<2){
            return s;
        }
        List<StringBuilder> tmp=new ArrayList<StringBuilder>();
        for (int i = 0;i<numRows;i++){
            tmp.add(new StringBuilder());
        }
        int i=0;
        int flag=-1;
        for (char c:s.toCharArray()){
            tmp.get(i).append(c);
            if (i==0 || i==numRows-1){
                flag=-flag;
            }
            i+=flag;
        }
        StringBuilder res=new StringBuilder();
        for (StringBuilder c: tmp){
            res.append(c);
        }
        return res.toString();
    }
}
```

### 扩展

### 其他优秀解答 





