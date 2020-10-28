package threads;

/**
 * @Author: Mr Liu Meng
 * @Date : 17:04 2020/10/28
 * @Description：
 */
public class ThreadTest {
    public static final int DELAY=0;
    public static final int STEPS=100;
    public static final double MAX_AMOUNT=1000;

    public static void main(String[] args){
        Bank bank=new Bank(4,1000);
        Runnable task1=() ->{
            try {
                while (true){
                    double amount=MAX_AMOUNT *Math.random();
                    bank.transfer(0,1,amount);
                    Thread.sleep((int)(DELAY*Math.random()));
                }
            }catch (InterruptedException e){

            }
        };

        Runnable task2=() ->{
            try {
                while (true){
                    double amount=MAX_AMOUNT*Math.random();
                    bank.transfer(2,3,amount);
                    Thread.sleep((int)(DELAY*Math.random()));
                }
            }catch (InterruptedException e){

            }
        };
        new Thread(task1).start();
        new Thread(task2).start();
    }
}
