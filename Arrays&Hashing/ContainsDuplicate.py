
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        if (nums == None):
            return False
        my_dict = {}
        for i in range(0, len(nums)):
            value = nums[i]
            if value in my_dict:
                return True
            my_dict[value] = 1
            # print(my_dict)
        return False
# Solution 클래스의 인스턴스를 생성
solution = Solution()
print(solution.hasDuplicate([1,2,3,4]))
print(solution.hasDuplicate([1,2,3,3]))
print(ord(' ') - 97)