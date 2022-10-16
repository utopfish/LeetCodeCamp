package string.c0115
class Solution {
    public static String s,t;
    public static int count;
    public void helper(int x,int y){
        if (y==t.length()){
            count++;
            return ;
        }
        if(x<s.length() && y<t.length()){
            for (int i=x;i<s.length();i++){
                if (s.charAt(i)==t.charAt(y)){
                    helper(x+1,y+1);
                }
            }
        }

    }
    public int numDistinct(String s, String t) {
        this.s=s;
        this.t=t;
        count=0;
        helper(0, 0);
        return count;
    }
    public static void main(String[] args){
        String s="rabbbit";
        String t="rabbit";
        Solution so=new Solution();
        System.out.println(so.numDistinct(s,t));
    }
}