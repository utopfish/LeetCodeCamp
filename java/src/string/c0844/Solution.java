package c0844;

class Solution {
    public boolean backspaceCompare(String S, String T) {
        return build(S).equals(build(T));
    }
    public String build(String s){
        StringBuilder n=new StringBuilder();
        char [] c=s.toCharArray();
        for (int i=0;i<s.length();i++){
            if (c[i]!='#'){
                n.append(c[i]);
            }else{
                if (n.length()>0){
                    n.deleteCharAt(n.length()-1);
                }
            }
        }
        return n.toString();
    }

}

class test{
    public static void  main(String[] args){
        String S="ab#c";
        String T="ad#c";
        Solution s=new Solution();
        System.out.println(s.backspaceCompare(S,T));
    }
}