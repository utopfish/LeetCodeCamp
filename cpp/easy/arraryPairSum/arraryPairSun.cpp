//
// Created by pro on 2019/12/3.
//

class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        int ans = 0;
        sort(nums.begin(), nums.end()); //将数组从小到大排列
        for(int i = 0; i < nums.size(); i = i +2) //将每对的第一位数相加
            ans = ans + nums[i];
        return ans;
    }
};