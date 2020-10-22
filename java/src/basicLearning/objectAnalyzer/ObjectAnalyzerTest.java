package objectAnalyzer;

import java.util.ArrayList;
import java.util.List;

/**
 * @Author: Mr Liu Meng
 * @Date : 18:23 2020/10/22
 * @Description： 用于任意类的通用 toString 方法测试
 */
public class ObjectAnalyzerTest {
    public static void main(String[] args) throws ReflectiveOperationException{
        ArrayList<Integer> squares =new ArrayList<Integer>();
        for (int i=0;i<=5;i++){
            squares.add(i*i);
        }
        System.out.println(new ObjectAnalyzer().toString(squares));
    }
}
