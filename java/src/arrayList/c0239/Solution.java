package c0239;

import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;

/**
 * @Author: Mr Liu Meng
 * @Date : 13:28 2021/1/4
 * @Description：
 */
public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> list=new LinkedList<Integer>();
        PriorityQueue<Integer> queue=new PriorityQueue<Integer>();
        int count=0;
        for (int i =0;i<k;i++){
            queue.add(nums[count]);
            count++;
        }
        list.add(queue.peek());
        for (int i=0;i<nums.length-k;i++){
            queue.remove(nums[count-k]);
            queue.add(nums[count]);
            list.add(queue.peek());
            count++;
        }
        return list;
    }
}
