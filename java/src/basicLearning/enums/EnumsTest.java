package enums;

import java.util.Scanner;

/**
 * @Author: Mr Liu Meng
 * @Date : 21:31 2020/10/22
 * @Description：
 */
public class EnumsTest {
    public static  void  main(String[] args){
        Scanner in =new Scanner(System.in);
        System.out.print("Enter a size: (SMALL,MEDIUM,LARGE,EXTRA_LARGE)");
        String input=in.next().toUpperCase();
        //将size 设置为Size.SMALL （SAMLL由in来确定）
        Size size=Enum.valueOf(Size.class,input);
        System.out.println("size="+size);
        System.out.println("abbreviation="+size.geAbbreviation());
        //enums_s.Size.values()返回包含全部枚举类的数组。
        Size [] values=Size.values();
        System.out.println(Size.values().toString());
        if(size==Size.EXTRA_LARGE){
            System.out.println("Good job--you paid attention to the _.");
        }
    }
}
enum Size{
    SMALL("S"),MEDIUM("M"),LARGE("L"),EXTRA_LARGE("XL");
    private Size(String abbreviation){this.abbreviation=abbreviation;}
    public String geAbbreviation(){return abbreviation;};
    private String abbreviation;
}

