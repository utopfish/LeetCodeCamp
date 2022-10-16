package basicLearning.multithread;

import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

public class Demo1 implements Runnable{
    private static AtomicInteger currentCount = new AtomicInteger(0);

    private static final Integer MAX_COUNT = 30;

    private static String [] chars = {"a", "b", "c"};

    private String name;

    public Demo1(String name) {
        this.name =  name;
    }

    @Override
    public void run() {
        while(currentCount.get()<MAX_COUNT){
            if(this.name.equals(chars[currentCount.get()%3])){
                printAndPlusOne(this.name + "\t" + currentCount);
            }
        }
    }

    public void printAndPlusOne(String content){
        System.out.println(content);
        currentCount.getAndIncrement();
    }

    public static void main(String [] args){
        ThreadPoolExecutor threadPoolExecutor = new ThreadPoolExecutor(3, 3, 20, TimeUnit.MINUTES, new LinkedBlockingQueue<Runnable>());
        threadPoolExecutor.execute(new Demo1("a"));
        threadPoolExecutor.execute(new Demo1("b"));
        threadPoolExecutor.execute(new Demo1("c"));
        threadPoolExecutor.shutdown();
    }
}

