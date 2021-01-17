package LCP5563;

import java.util.PriorityQueue;

/**
 * @Author: Mr Liu Meng
 * @Date : 11:59 2020/11/8
 * @Description：
 */
public class Solution {
    public int maxProfit(int[] inventory, int orders) {
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
        for (int i=0;i<inventory.length;i++){
            queue.offer(-inventory[i]);
        }

        double count=0;
        while (orders>0){
            int top1=-queue.poll();
            int top2=0;
            if (!queue.isEmpty()){
                top2=-queue.peek();
            }
            int range_length=Math.min(top1-top2+1,orders);
            count+=((top1-range_length+1+top1)*range_length/2);
            count = count % (1000000000+7);
            orders-=range_length;
            queue.offer(-(top2-1));
        }
        return (int)count;
    }
    public static void main(String[] args){
//        int [] v=new int[]{773160767};
//        int o=252264991;
//        Solution s=new Solution();
//        System.out.print(s.maxProfit(v,o));
        for (int i=0;i<50;i++){
            System.out.println(1<<i);
        }
    }
}
