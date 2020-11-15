package c0922;

/**
 * @Author: Mr Liu Meng
 * @Date : 9:01 2020/11/12
 * @Description：
 */
public class Solution {
    public void swap(int[] arr,int i,int j){
        int tmp=arr[i];arr[i]=arr[j];arr[j]=tmp;
    }
    public int[] sortArrayByParityII(int[] A) {
        int i=0,j=1;
        int len=A.length;
        while (i<len && j<=len){
            while( A[i]%2==0) {
                i+=2;
                if (i>len-1){
                    break;
                }
            }
            while( A[j]%2==1) {
                j+=2;
                if (j>len-1){
                    break;
                }
            }
            if (i<len && j<len){
                swap(A,i,j);
            }
        }
        return A;
    }
    public static void main(String[] args){
        int[] input=new int[]{3,4};
        Solution s=new Solution();
        System.out.print(s.sortArrayByParityII(input));
    }
}
