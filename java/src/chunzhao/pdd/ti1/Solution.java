package chunzhao.pdd.ti1;

import java.util.Scanner;
public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k=in.nextInt();
        int []arr=new int[k];
        for (int i=0;i<k;i++){
            arr[i]=in.nextInt();
        }
        int res=0;
        int left=0;
        while(left+2<k) {
            int right = left + 1;
            if (arr[left] < arr[left + 1]) {
                while (right + 1 < k && arr[right] < arr[right + 1]) {
                    right++;
                }
                if (right < k - 1 && arr[right] > arr[right + 1]) {
                    while (right+1<k && arr[right]>arr[right+1]){
                    right++;
                }
                res = Math.max(res, right - left + 1);
            } else {
                right++;
            }
        }
            left=right;
        }
        System.out.println(res);
    }

}
