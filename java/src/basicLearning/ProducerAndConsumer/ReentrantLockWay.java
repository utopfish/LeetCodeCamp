package ProducerAndConsumer;


import java.util.LinkedList;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * @Author: Mr Liu Meng
 * @Date : 15:15 2020/12/1
 * @Description：
 */

public class ReentrantLockWay {
    private static Buffer buffer =new Buffer();
    public static void main(String[] args){
        ExecutorService executor = Executors.newFixedThreadPool(2);
        executor.execute(new ProducerTask());
        executor.execute(new ConsumerTask());
        executor.shutdown();
    }
    // A task for adding an int to the buffer
    private static class ProducerTask implements Runnable{
        @Override
        public void run(){
            try {
                int i=1;
                while (true){
                    System.out.println("Producer writes "+i);
                    buffer.write(i++);
                    Thread.sleep((int)(Math.random()*10000));
                }
            }catch (InterruptedException ex){
                ex.printStackTrace();
            }
        }
    }
    //A task for reading and deleteing an int form the buffer
    private static class ConsumerTask implements Runnable{
        @Override
        public void run(){
            try {
                while (true){
                    System.out.println("Consumer reads "+buffer.read());
                    Thread.sleep((int)(Math.random()*10000));
                }
            }catch (InterruptedException ex){
                ex.printStackTrace();
            }
        }
    }
    //An inner class for buffer
    private static class Buffer{
        private static final int CAPACITY= 1;//buffer size
        private LinkedList<Integer> queue=new LinkedList<Integer>();
        //Create a new lock
        private static Lock lock =new ReentrantLock();

        //Create tow condition
        private static Condition notEmpty =lock.newCondition();
        private static Condition notFull= lock.newCondition();

        public void write(int value){
            lock.lock();
            try {
                while (queue.size()==CAPACITY){
                    System.out.println("Wait for notFull condition");
                    notFull.await();
                }
                queue.offer(value);
                notEmpty.signal();
            }catch (InterruptedException ex){
                ex.printStackTrace();
            }finally {
                lock.unlock();
            }
        }
        public int read(){
            int value=0;
            lock.lock();
            try {
                while (queue.isEmpty()){
                    System.out.println("Wait for notEmpty condition");
                    notEmpty.await();
                }
                value=queue.remove();
                notFull.signal();
            }catch (InterruptedException ex){
                ex.printStackTrace();
            }finally {
                lock.unlock();
                return value;
            }
        }

        }

}
