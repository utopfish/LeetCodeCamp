package chunzhao.meituan.ti5;

import java.util.*;
public class Main {
    private static int maxP=0;
    public  static void DFS(int x, List<List<Integer>> map, int count, int[] height,int[]visited){
        List<Integer> node=map.get(x);
        for (int i=0;i<node.size();i++){
            int next=node.get(i);
            if (visited[next]==0 && height[next]<=height[x]){
                visited[next]=1;
                maxP=Math.max(maxP,count+1);
                DFS(next,map,count+1,height,visited);
                visited[next]=0;
            }
        }
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        int n=sc.nextInt();
        int []visited=new int[n];
        int m=sc.nextInt();
        int [] height=new int[n];
        for (int i=0;i<n;i++){
            height[i]=sc.nextInt();
        }
        int [][]v=new int[m][2];
        for (int i=0;i<m;i++){
            v[i][0]=sc.nextInt()-1;
            v[i][1]=sc.nextInt()-1;
        }
        List<List<Integer>> map=new LinkedList<List<Integer>>();
        for (int i=0;i<n;i++){
            List<Integer> temp=new LinkedList<Integer>();
            for (int j=0;j<m;j++){
                if (v[j][0]==i){
                    temp.add(v[j][1]);
                }else if (v[j][1]==i){
                    temp.add(v[j][0]);
                }
            }
            map.add(temp);
        }
        for (int i=0;i<n;i++){
            visited[i]=1;
            DFS(i,map,1,height,visited);
            visited[i]=0;
        }
        System.out.println(maxP);
    }
}
