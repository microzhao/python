#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(len(nums) < 1):return 0
        index=0
        while index < len(nums):
            if (nums[index] >= target):
                return index
            index = index+1
        return index
