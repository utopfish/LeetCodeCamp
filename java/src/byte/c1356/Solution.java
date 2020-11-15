package c1356;

/**
 * @Author: Mr Liu Meng
 * @Date : 10:35 2020/11/6
 * @Description：
 */
public class Solution {
    private static boolean less(int v,int w){
        int tmpV=v;
        int tmpW=w;
        int countV=0;
        int countW=0;
        while (v !=0){
            if ((v&1)==1){
                countV++;
            }
            v>>=1;
        }
        while (w>0){
            if ((w&1)==1){
                countW++;
            }
            w>>=1;
        }
        if (countV!=countW) {
            return countV<countW;
        } else {
            return tmpV<tmpW;
        }
    }
    private static void exch(int[] a,int i,int j){
        int t=a[i];a[i]=a[j];a[j]=t;
    }
    private static void sort(int[] a,int lo,int hi){
        if (hi<=lo) return;
        int j=partition(a,lo,hi);
        sort(a,lo,j-1);
        sort(a,j+1,hi);
    }
    private static int partition (int[] a,int lo,int hi){
        int i=lo,j=hi+1;
        int v=a[lo];
        while(true){
            while (less(a[++i],v)) if (i==hi) break;
            while (less(v,a[--j])) if (j==lo) break;
            if (i>=j) break;
            exch(a,i,j);
        }
        exch(a,lo,j);
        return j;
    }
    public int[] sortByBits(int[] arr) {
        sort(arr,0,arr.length-1);
        return arr;
    }
    public static void main(String[] args){
        int [] arr=new int[]{0,1,2,4};
        Solution s=new Solution();
        System.out.print(s.sortByBits(arr).toString());
    }
}
