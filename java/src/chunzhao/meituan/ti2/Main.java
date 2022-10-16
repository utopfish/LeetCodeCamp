package chunzhao.meituan.ti2;

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        s=s.trim();
        List<String> res=new LinkedList<String>();
        String temp="";
        for (int i=0;i<s.length();i++){
            if (s.charAt(i)>=48 && s.charAt(i)<=57){
                temp+=s.charAt(i);
            }else {
                if (temp.length()>0){
                    res.add(temp);
                    temp="";
                }
            }
        }
        if (temp.length()>0)res.add(temp);
        Collections.sort(res, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length()==o2.length()){
                    return Integer.valueOf(o1)-Integer.valueOf(o2);
                }
                return o1.length()-o2.length();
            }
        });
        for (int i=0;i<res.size();i++){
            System.out.println(res.get(i));
        }
    }
}