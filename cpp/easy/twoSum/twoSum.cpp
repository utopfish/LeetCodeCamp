#include <map>
#include <vector>
#include <iostream>
using namespace std;

//
// Created by pro on 2019/11/18.
//
class Solution{
public:
    vector<int> twoSum(vector<int>&nums,int target){
        map<int,int> a;
        vector<int> b(2,-1);
        for (int i=0;i<nums.size();i++){
            if (a.count(target-nums[i])>0){
                b[0]=a[target-nums[i]];
                b[1]=i;
                break;
            }
            a[nums[i]]=i;
        }
        return b;
    };
};
int main(){
    vector<int> nums={2, 7, 11, 15};
    int target=9;
    Solution test;
    vector<int> re=test.twoSum(nums,target);
    for (int i=0;i<re.size();i++){
        printf("%d ",re[i]);
    }

}