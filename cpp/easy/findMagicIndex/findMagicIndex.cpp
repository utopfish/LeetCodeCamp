//
// Created by pro on 2020/7/31.
//
//最基础的做法
class Solution1 {
public:
    int findMagicIndex(vector<int>& nums) {
        for (int i=0 ;i<nums.size();i++){
            if (i==nums[i]){
                return i;
            }
        }
        return -1;
    }
};
//二分查找
class Solution2 {
public:
    int getAnswer(vector<int>& nums, int left, int right) {
        if (left > right) {
            return -1;
        }
        int mid = (right - left) / 2 + left;
        int leftAnswer = getAnswer(nums, left, mid - 1);
        if (leftAnswer != -1) {
            return leftAnswer;
        } else if (nums[mid] == mid) {
            return mid;
        }
        return getAnswer(nums, mid + 1, right);
    }

    int findMagicIndex(vector<int>& nums) {
        //注意这里-1 否则可能出现越界
        return getAnswer(nums, 0, (int) nums.size() - 1);
    }
};


