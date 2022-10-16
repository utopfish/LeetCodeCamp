package chunzhao.pdd.ti2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int flag=-1;
        for (int i=1;i<100;i++){
            int temp=n*i;
            flag=-1;
            while(temp>0){
                if (temp%10!=0 &&temp%10!=1){
                    if (flag==-1)flag=temp%10;
                    else break;
                }
                temp=temp/10;
            }
            if (temp==0){
                System.out.print(n*i);
                break;
            }
        }
    }
}
