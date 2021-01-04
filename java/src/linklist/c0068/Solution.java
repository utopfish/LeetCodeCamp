package c0068;

import c0024swapPairs.ListNode;

/**
 * @Author: Mr Liu Meng
 * @Date : 13:56 2021/1/4
 * @Description：
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode small=new ListNode();
        ListNode big=new ListNode();
        ListNode b=big;
        ListNode s=small;
        while (head!=null){
            if (head.val<x){
                small.next=new ListNode(head.val);
                small=small.next;
            }else{
                big.next=new ListNode(head.val);
                big=big.next;
            }
            head=head.next;
        }
        small.next=b.next;
        return s.next;

    }
}
