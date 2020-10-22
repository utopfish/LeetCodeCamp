package innerClass;
import java.awt.*;
import java.awt.event.*;
import java.time.*;

import javax.swing.*;
/**
 * @Author: Mr Liu Meng
 * @Date : 21:32 2020/10/22
 * @Description：
 */
public class InnerClassTest {
    public static void main(String[] args){
        TalkingClock clock=new TalkingClock(1000,true);
        clock.start();

        JOptionPane.showMessageDialog(null,"Quit progarm?");
        System.exit(0);
    }
}
class TalkingClock{
    private int interval;
    private boolean beep;

    public TalkingClock(int interval,boolean beep){
        this.interval=interval;
        this.beep=beep;
    }

    public void start(){
        TimePrinter listener=new TimePrinter();
        Timer timer=new Timer(interval,listener);
        timer.start();
    }
    //使用内部类，TimePrinter 拿到了TalkingClock的私有变量beep。
    //这样就不需要提供仅用于另一个类的访问器了
    public class TimePrinter implements ActionListener{
        public void actionPerformed(ActionEvent event){
            System.out.println("At the tone, this time is "
            +Instant.ofEpochMilli(event.getWhen()));
            if (beep) Toolkit.getDefaultToolkit().beep();
        }
    }
}

