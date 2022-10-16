package chunzhao.meituan.ti3;

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        int [] nums=new int[n];
        for (int i=0;i<n;i++){
            nums[i]=sc.nextInt();
        }
        List<int[]> count;
        HashMap<Integer,Integer> hm;
        for (int i=0;i<n-k+1;i++){
            count=new LinkedList<>();
            hm=new HashMap<Integer,Integer>();
            for (int j=0;j<k;j++){
                hm.put(nums[i+j],hm.getOrDefault(nums[i+j],0)+1);
            }
            for (HashMap.Entry<Integer,Integer> entry:hm.entrySet()){
                count.add(new int[]{entry.getKey(),entry.getValue()});
            }
            Collections.sort(count, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    if (o1[1]==o2[1]){
                        return o1[0]-o2[0];
                    }else{
                        return o2[1]-o1[1];
                    }
                }
            });
            System.out.println(count.get(0)[0]);
        }

    }
}