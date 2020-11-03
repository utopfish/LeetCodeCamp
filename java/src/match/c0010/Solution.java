package c0010;

/**
 * @Author: Mr Liu Meng
 * @Date : 16:07 2020/11/3
 * @Description：
 */
public class Solution {
    public boolean isMatch(String s, String p) {
        if (s == null || p == null) {
            return false;
        }
        boolean [][] dp=new boolean[s.length()+1][p.length()+1];
        dp[0][0]=true;
        //"" 和p的匹配关系初始化，a*a*a*a*a*这种能够匹配空串，其他的是都是false。
        //  奇数位不管什么字符都是false，偶数位为* 时则: dp[0][i] = dp[0][i - 2]
        for (int j = 0; j < p.length(); j++) { // here's the p's length, not s's
            if (p.charAt(j) == '*' && dp[0][j - 1]) {
                dp[0][j + 1] = true; // here's y axis should be i+1
            }
        }
        for (int i=1;i<=s.length();i++){
            for (int j=1;j<=p.length();j++){
                if (p.charAt(j-1)==s.charAt(i-1) || p.charAt(j-1)=='.'){//任意元素进行匹配
                    dp[i][j]=dp[i-1][j-1];
                }else if (p.charAt(j-1)=='*'){
                    if (p.charAt(j-2)==s.charAt(i-1) || p.charAt(j-2)=='.'){
                        dp[i][j]=dp[i-1][j] || dp[i-1][j-2] || dp[i][j-2];
                        /*
                            dp[i][j] = dp[i-1][j] // 多个字符匹配的情况
                            or dp[i][j] = dp[i][j-1] // 单个字符匹配的情况
                            or dp[i][j] = dp[i][j-2] // 没有匹配的情况
                             */
                    }else {
                        dp[i][j]=dp[i][j-2];//没有匹配
                    }
                }
            }
        }
        return dp[s.length()][p.length()];
    }
    public static void  main(String[] args){
        String s="ab";
        String p=".*";
        Solution t=new Solution();
        System.out.print(t.isMatch(s,p));

    }
}
