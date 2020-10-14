public class test_int {
    public static  void main(String[] args){
        //精度丢失，1.23456792E8
        int n=123456789;
        float f=n;
        System.out.println(f);
        //8个字符，两位小数的精度，123456792.00
        System.out.printf("%8.2f",f);
        System.out.println();
        //增加分组分割符，123,456,792.00
        System.out.printf("%,.2f",f);
    }
}
