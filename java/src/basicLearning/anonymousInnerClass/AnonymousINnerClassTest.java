package anonymousInnerClass;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.time.*;

import javax.swing.*;

/**
 * @Author: Mr Liu Meng
 * @Date : 21:54 2020/10/22
 * @Description：
 */
public class AnonymousINnerClassTest {
    public static  void main(String[] args){
        TalkingClock clock=new TalkingClock();
        clock.start(1000,true);

        JOptionPane.showMessageDialog(null,"Quit progarm?");
        System.exit(0);
    }
}
class TalkingClock{
    public void  start(int interval,boolean beep){
        ActionListener listener=new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("At the tone, the time is "
                + Instant.ofEpochMilli(e.getWhen()));
                if(beep) Toolkit.getDefaultToolkit().beep();
            }
        };
        Timer timer=new Timer(interval,listener);
        timer.start();
    }
}
