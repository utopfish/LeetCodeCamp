from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        记录头和尾
        """
        start,end=0,0
        while start+end!=len(nums):
            if nums[start]==0:
                nums.append(nums.pop(start))
                start-=1
                end+=1
            start+=1
        return nums


if __name__=="__main__":
    Test=Solution()
    print(Test.moveZeroes([0,0,1]))