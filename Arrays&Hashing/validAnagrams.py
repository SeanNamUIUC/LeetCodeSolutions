# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # True -> if an array that has a length of 26 filled with 0s 
        # Iterate through s, t 
        # add 1 by iterating through each character
        # subtract 1 by iterating through each character

        if (len(s) != len(t)): 
            return False
        my_list = [0] * 26
        for i in range(0, len(s)):
            # ascii code -> 65: 'A' , 97 : 'a'
            idx = ord(s[i]) - 97
            my_list[idx] += 1
        for i in range(0, len(t)):
            # ascii code
            idx = ord(t[i]) - 97
            my_list[idx] -= 1
        for i in range(0, len(my_list)):
            if(my_list[i] != 0):
                return False
        return True
Solution = Solution()        
print(Solution.isAnagram("jar", "jam"))
print(Solution.isAnagram("jar", "jar"))