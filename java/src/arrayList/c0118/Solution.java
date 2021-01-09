import java.util.LinkedList;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ret=new LinkedList<List<Integer>>();
        for(int i=0;i<numRows;i++){
            int tmp=0;
            if (i==0){
                List<Integer> preList=new LinkedList<Integer>();
                preList.add(1);
                ret.add(preList);
                continue;
            }
            List<Integer> preList=ret.get(i-1);
            List<Integer> tmpList=new LinkedList<Integer>();
            while(tmp<=i){
                if (tmp==0 || tmp==i){
                    tmpList.add(1);
                }
                else{

                    int preNode=preList.get(tmp-1);
                    int nextNode=preList.get(tmp);
                    tmpList.add(preNode+nextNode);
                }
                tmp++;
            }
            ret.add(tmpList);

        }
        return ret;
    }
    public static void main(String[] args){
        Solution s=new Solution();
        System.out.println(s.generate(5));
    }
}
