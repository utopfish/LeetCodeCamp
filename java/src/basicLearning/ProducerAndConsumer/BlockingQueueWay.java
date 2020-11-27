package ProducerAndConsumer;

import sun.awt.windows.ThemeReader;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

/**
 * @Author: Mr Liu Meng
 * @Date : 16:11 2020/11/25
 * @Description：
 */
public class BlockingQueueWay {
    private static int count = 0;
    final BlockingQueue blockingQueue = new ArrayBlockingQueue<>(10);
    public static void main(String [] args){
        BlockingQueueWay test = new BlockingQueueWay();
        new Thread(test.new Producer()).start();
        new Thread(test.new Producer()).start();
        new Thread(test.new Consumer()).start();
        new Thread(test.new Producer()).start();
        new Thread(test.new Consumer()).start();
        new Thread(test.new Producer()).start();
        new Thread(test.new Consumer()).start();
        new Thread(test.new Producer()).start();
        new Thread(test.new Consumer()).start();
    }
    class Producer implements Runnable {
        @Override
        public void run(){
            for (int i =0 ; i<10 ; i++){
                try {
                    Thread.sleep(3000);
                }catch (Exception e){
                    e.printStackTrace();
                }
                try {
                    blockingQueue.put(1);
                    count++;
                    System.out.println(Thread.currentThread().getName()+"生产者生产，目前共有"+count);
                }catch (Exception e){
                    e.printStackTrace();
                }
            }
        }
    }
    class Consumer implements Runnable {
        @Override
        public void run(){
            for (int i = 0; i < 10; i++){
                try {
                    Thread.sleep(3000);
                }catch (Exception e){
                    e.printStackTrace();
                }
                try {
                    blockingQueue.poll();
                    count--;
                    System.out.println(Thread.currentThread().getName()+"消费者消费，目前共有"+count);
                }catch (Exception e){
                    e.printStackTrace();
                }
            }
        }
    }
}
