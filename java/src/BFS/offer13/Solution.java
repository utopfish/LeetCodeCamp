package BFS.offer13;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int movingCount(int m, int n, int k) {
        Queue<int[]> queue=new LinkedList<int[]>();
        queue.add(new int[]{0,0});
        boolean[][] visited=new boolean[m][n];
        visited[0][0]=true;
        int count=1;
        int x;
        int y;
        int temp[][]={{0,1},{1,0}};
        while(!queue.isEmpty()){
            int t[]=queue.poll();
            x=t[0];
            y=t[1];
            for (int i=0;i<2;i++){
                int new_x=x+temp[i][0];
                int new_y=y+temp[i][1];
                if (-1<new_x && new_x<m && -1<y && y<n){
                    int sum=0;
                    while(new_x!=0){
                        sum+=new_x%10;
                        new_x/=10;
                    }
                    while(new_y!=0){
                        sum+=new_y%10;
                        new_y/=10;
                    }
                    if (k>=sum){
                        if (!visited[x+temp[i][0]][y+temp[i][1]]){
                            queue.add(new int[]{x+temp[i][0],y+temp[i][1]});
                            count+=1;
                            visited[x+temp[i][0]][y+temp[i][1]]=true;
                        }
                    }
                }
            }

        }
        return count;
    }
    public static void main(String [] args){
        Solution s=new Solution();
        System.out.println(s.movingCount(3,3,17));
    }
}
