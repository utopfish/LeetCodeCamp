package c0547;

import java.util.HashSet;
import java.util.Set;

/**
 * @Author: Mr Liu Meng
 * @Date : 10:21 2021/1/7
 * @Description：
 */
public class Solution {
    public int findCircleNum(int[][] isConnected) {
        UnionFind uf=new UnionFind(isConnected.length);
        for (int i=0;i<isConnected.length;i++){
            for (int j=i+1;j<isConnected.length;j++){
                if (isConnected[i][j]==1){
                    uf.union(i, j);
                }
            }
        }
        return uf.getSize();

    }
    public class UnionFind{
        private int [] parent;

        public  UnionFind(int n){
            this.parent=new int[n];
            for (int i=0;i<n;i++){
                parent[i]=i;
            }
        }
        public int find(int x){
            if (x!=parent[x]){
                parent[x]=find(this.parent[x]);
            }
            return parent[x];
        }
        public void union(int x,int y){
            int rootX=find(x);
            int rootY=find(y);
            if (rootX!=rootY){
                parent[rootX]=rootY;
            }
        }
        public int getSize(){
            int count=0;
            for (int i=0;i<parent.length;i++){
                if (parent[i]==i){
                    count++;
                }
            }
            return count;
        }
    }
    public static void main(String[] args){
        Solution s=new Solution();
        //int a[][]={{1,0,0,1},{0,1,1,0},{0,1,1,1},{1,0,1,1}};
        //int a[][]={{1,1,0},{1,1,0},{0,0,1}};
        int a[][]={{1,0,0},{0,1,0},{0,0,1}};
        System.out.println(s.findCircleNum(a));
    }
}
