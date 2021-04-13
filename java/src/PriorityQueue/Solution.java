package PriorityQueue;
import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * @Author: Mr Liu Meng
 * @Date : 9:35 2020/11/9
 * @Description：
 */

public class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> queue = new PriorityQueue<int[]>(new Comparator<int[]>() {
            public int compare(int[] arr1, int[] arr2) {
                return (arr2[0] * arr2[0] + arr2[1] * arr2[1])-(arr1[0] * arr1[0] + arr1[1] * arr1[1]);
            }
        });
        for (int i=0;i<points.length;i++){
            if (queue.size()>=K){
                int []tmp=queue.peek();
                int dist=tmp[0] * tmp[0]+tmp[1] * tmp[1];
                if (points[i][0]*points[i][0]+points[i][1]*points[i][1]<dist){
                    queue.poll();
                    queue.offer(points[i]);
                }
            }else{
                queue.offer(points[i]);
            }
        }
        int [][]ret=new int[K][2];
        for (int i=0;i<K;i++){
            ret[i]=queue.poll();
        }
        return ret;
    }
    public static void main(String[] args){
        int [][] point=new int[][]{{1,3},{-2,2}};
        int K=1;
        Solution s=new Solution();
        System.out.print(s.kClosest(point,K).toString());
    }

}
