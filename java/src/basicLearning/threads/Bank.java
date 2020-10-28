package threads;

import java.util.Arrays;

/**
 * @Author: Mr Liu Meng
 * @Date : 17:14 2020/10/28
 *
 */
/*
A bank with a number of account
*/


public class Bank {
    private final double [] accounts;

    /*
    * Constructs the bank
    * @param n the number of account
    * @param initialBalance the initial balance for each account
    * */
    public Bank(int n,double initalBalance){
        accounts=new double[n];
        Arrays.fill(accounts,initalBalance);
    }
    public synchronized void transfer(int from,int to,double amount) throws InterruptedException{
        while (accounts[from]<amount){
            wait();
        }

        System.out.print(Thread.currentThread());
        accounts[from]-=amount;
        System.out.printf("%10.2f from %d to %d",amount,from,to);
        accounts[to]+=amount;
        notifyAll();
        //%n change line
        System.out.printf("  Total Balance: %10.2f%n",getTotalBlance());
    }
    public synchronized double getTotalBlance(){
        double sum=0;
        for (double a:accounts){
            sum+=a;
        }
        return sum;
    }
    public int size(){
        return accounts.length;
    }
}
