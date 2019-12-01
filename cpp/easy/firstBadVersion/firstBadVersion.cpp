//
// Created by pro on 2019/12/1.
//
bool isBadVersion(int version);

class Solution {//二分查找
public:
    int firstBadVersion(int n) {
        int low = 1;
        int high =n;
        int mid=n;
        while(low<high)
        {
            mid = low +( high - low)/2;//减少越界的可能性
            if(isBadVersion(mid))
                high = mid;
            else low = mid + 1;
        }
        return high;
    }
};

