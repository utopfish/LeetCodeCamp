import java.util.Arrays;
import java.util.List;
import java.util.stream.StreamSupport;

/**
 * @Author: Mr Liu Meng
 * @Date : 15:40 2020/11/2
 * @Description：
 */
public class typeChange {
    public static void main(String[] args){
        String[] s = new String[]{"A", "B", "C", "D","E"};
        List<String> list = Arrays.asList(s);
        System.out.print(list);

        String[] dest = list.toArray(new String[0]);//new String[0]是指定返回数组的类型
        System.out.println("dest: " + Arrays.toString(dest));


        Integer[] i = new Integer[]{1, 2, 3};
        List<Integer> list2 = Arrays.asList(i);
        System.out.print(list2);

//        String[] dest = list.toArray(new String[0]);//new String[0]是指定返回数组的类型
//        System.out.println("dest: " + Arrays.toString(dest));
    }
}
