# Two Sum
# Solved 
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]
# Constraints:

# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_list = {}
        for i in range(0, len(nums)):
            val = nums[i]
            find = target - val
            if val in my_list:
                idx1 = my_list[val]
                return [idx1, i]
            my_list[find] = i #{6:0, 5:1, 4:2 }
Solution = Solution()
print(Solution.twoSum([4,5,6,7] , 10))