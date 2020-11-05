package c0127;

import java.util.*;

/**
 * @Author: Mr Liu Meng
 * @Date : 15:32 2020/11/5
 * @Description：
 */
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        //List转为Set加速查找
        HashSet<String> wordSet = new HashSet<String>(wordList);
        //广度优先队列进行遍历
        Queue<String> queue = new LinkedList<String>();
        queue.add(beginWord);
        //使用一个HashSet记录访问过的节点
        HashSet<String> visited = new HashSet<String>();
        visited.add(beginWord);
        int step = 1;
        while (!queue.isEmpty()) {
            int currentSize = queue.size();
            for (int i = 0; i < currentSize; i++) {
                String word = queue.poll();
                char[] chars = word.toCharArray();
                for (int j = 0; j < word.length(); j++) {
                    char originChar = chars[j];
                    for (char k = 'a'; k <= 'z'; k++) {
                        if (k == originChar) {
                            continue;
                        }
                        chars[j] = k;
                        String tmpWord = String.valueOf(chars);
                        if (wordSet.contains(tmpWord)) {
                            if (tmpWord.equals(endWord)) {
                                return step + 1;
                            }
                            if (!visited.contains(tmpWord)) {
                                visited.add(tmpWord);
                                queue.add(tmpWord);
                            }
                        }

                    }
                    chars[j]=originChar;
                }
            }
            step++;
        }
        return 0;
    }
    public static void main(String[] args){
        String beginWord = "hit";
        String endWord = "cog";
        List<String>wordList = new ArrayList<>();
        Collections.addAll(wordList,"hot","dot","dog","lot","log","cog");
        Solution s=new Solution();
        System.out.print(s.ladderLength(beginWord,endWord,wordList));

    }
}