package lambda;

import java.util.Arrays;
import java.util.Date;
import javax.swing.*;

/**
 * @Author: Mr Liu Meng
 * @Date : 20:48 2020/10/22
 * @Description：
 */
public class LambdaTest {
    public static void main(String[] args){
        String[] planets=new String[]{"Mercury","Venus","Earth","Mars",
        "Jupiter","Saturn","Ueanus","Neptune"};
        System.out.println(Arrays.toString(planets));
        System.out.println("Sorted in dictionary order:");
        Arrays.sort(planets);
        System.out.println(Arrays.toString(planets));
        System.out.println("Sorted by length:");
        Arrays.sort(planets,(first,second)->{return first.length()-second.length();});
        System.out.println(Arrays.toString(planets));


        Timer timer=new Timer(1000, event ->
        {System.out.println("This time is "+new Date());});
        timer.start();

        //keep program running until user selects "OK"
        JOptionPane.showMessageDialog(null,"Quit program?");
        System.exit(0);

    }
}
