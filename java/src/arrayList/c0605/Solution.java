package c0605;

/**
 * @Author: Mr Liu Meng
 * @Date : 13:09 2021/1/4
 * @Description：
 */
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count=0;
        for (int i =0;i<flowerbed.length;i++){
            if (flowerbed[i]==0 && ((i==0)||(i>0 && flowerbed[i-1]==0)) && (i==flowerbed.length-1||(i<flowerbed.length-1 && flowerbed[i+1]==0))){
                flowerbed[i]=1;
                count+=1;
            }
        }
        return (count>=n);
    }
    public static void main(String[] args){
        Solution s=new Solution();
        int []flowerbed = {1,0,0,0,1};
        int n=1;
        System.out.println(s.canPlaceFlowers(flowerbed,n));
    }
}
