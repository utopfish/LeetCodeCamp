package chunzhao.pdd.ti4;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m=sc.nextInt();
        HashMap<Integer,Integer> hm=new HashMap<>();
        List<Integer> num=new LinkedList<>();
        for (int i=m;i>1;i--){
            if (m%i==0){
                int count=0;
                int temp=n;
                while (temp!=0){
                    temp/=i;
                    count+=temp;
                }
                hm.put(i,count);
                num.add(i);
            }
        }
        hm.put(1,n);
        int res=0;
        for (int i=0;i<num.size();i++){
            if (m==num.get(i)||hm.containsKey(m/num.get(i))){
                int big=num.get(i);
                int bigCount=hm.get(big);
                int smallCount=hm.get(m/num.get(i));
                bigCount=Math.min(bigCount,smallCount);
                res+=bigCount;
                hm.put(big,0);
                hm.put(m/num.get(i),smallCount-bigCount);


                for (int j=big/2+1;j>1;j--){
                    if (big%j==0 && hm.containsKey(j)){
                        hm.put(j,hm.get(j)-bigCount);
                    }
                    if (big%j==0 && hm.containsKey((int)Math.sqrt(j))){
                        int tempInt= (int) Math.sqrt(big);
                        hm.put((int) Math.sqrt(j),hm.get((int)Math.sqrt(j))-bigCount);
                    }
                }

            }
        }
        System.out.println(res);
    }
}
