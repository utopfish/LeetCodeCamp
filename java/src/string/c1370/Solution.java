package c1370;

/**
 * @Author: Mr Liu Meng
 * @Date : 16:06 2020/11/25
 * @Description：
 */
public class Solution {
    public String sortString(String s) {
        int [] bucket = new int [26];
        for (char c : s.toCharArray()){
            bucket[c-'a']++;
        }
        char [] ret= new char [s.length()];
        int index = 0;
        while (index < s.length()){
            for (int i = 0; i < 26; i++){
                if (bucket[i] != 0){
                    ret[index++]=(char) (i+'a');
                    bucket[i]--;
                }
            }
            for (int i = 25; i >= 0; i--){
                if (bucket[i] != 0){
                    ret[index++]=(char) (i+'a');
                    bucket[i]--;
                }
            }
        }
        return new String(ret);
    }
    public static void  main(String[] args){
        String input = "gnvgnv";
        Solution s = new Solution();
        System.out.print(s.sortString(input));
    }

}
