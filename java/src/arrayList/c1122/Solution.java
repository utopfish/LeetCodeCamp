package c1122;

import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

/**
 * @Author: Mr Liu Meng
 * @Date : 10:47 2020/11/14
 * @Description：
 */
class Solution {
    public static void swap(int [] arr,int i,int j){
        int tmp=arr[i];arr[i]=arr[j];arr[j]=tmp;
    }
    public static int partition(int[] arr,int lo,int hi){
        int i=lo,j=hi+1;
        int v=arr[i];
        while (true){
            while(arr[++i]<v) if (i==hi)break;
            while(arr[--j]>v) if (j==lo) break;
            if (i>=j) break;
            swap(arr,i,j);
        }
        swap(arr,lo,j);
        return j;
    }
    public void sort(int[] arr,int lo,int hi){
        if (lo>=hi) return;
        int j=partition(arr,lo,hi);
        sort(arr,lo,j-1);
        sort(arr,j+1,hi);
    }
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int index=0;
        for (int i=0;i<arr2.length;i++){
            for (int j=index;j<arr1.length;j++){
                if (arr2[i]==arr1[j]){
                    if (j==index){
                        index++;
                    }else{
                        swap(arr1,j,index);
                        index++;
                    }
                }
            }
        }
        sort(arr1,index,arr1.length-1);
        return arr1;
    }
    public static void main(String[] args){
        int [] arr1=new int[]{28,6,22,8,44,17};
        int [] arr2=new int[]{22,28,8,6};
        Solution s=new Solution();
        System.out.print(s.relativeSortArray(arr1,arr2));
    }
}
