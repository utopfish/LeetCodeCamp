from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or target <= nums[0]:
            return 0
        for index in range(len(nums) - 1):
            if target == nums[index]:
                return index
            if target > nums[index] and target <= nums[index + 1]:
                return index + 1
        return len(nums)


if __name__ == "__main__":
    nums = [1,3]
    target = 3
    s = Solution()
    t = s.searchInsert(nums, target)
    print(t)
