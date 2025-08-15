# Products of Array Except Self
# Solved 
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #내 기준 왼쪽부터 바로 왼쪽 까지의 총 곱 과 오른쪽부터 바로 오른쪽까지의 총곱을 합한것?
        #[곱----> ㅑ  <--------곱]
        res = [1] * len(nums)
        wholeProduct = 1
        #O(n)
        fromLeft, fromRight = [1] * len(nums), [1] * len(nums)
        for i in range(0, len(nums)):
            wholeProduct *= nums[i]
            fromLeft[i] = wholeProduct
        wholeProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            wholeProduct *= nums[i]
            fromRight[i] = wholeProduct
        print(fromLeft, fromRight)

        res[0] = fromRight[1]
        res[len(nums) - 1] = fromLeft[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            res[i] = fromLeft[i - 1] * fromRight[i + 1]
        return res
        #original
        # [1, 2, 4 ,6]
        #from left
        # [1 ,2 ,8 ,48]
        #from right
        # [48, 48, 24, 6]