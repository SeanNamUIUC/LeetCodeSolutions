# Group Anagrams
# Solved 
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.



#Solution 1 -> Time Complexity: O(m * n^2), Space Complexity: O(m * n)
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
        
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        my_dict = {}
        for i in range(0,len(strs)):
            str1 = strs[i]
            #기존 그룹에 하나 더 넣을수 있는지 확인
            found = False
            for str2 in my_dict:
                if(self.isAnagram(str1, str2)):
                    print("str1 is ", str1)
                    print("str2 is ", str2)
                    found = True
                    my_dict[str2].append(str1)
                    break
            #아니라면 새로 추가 
            if not found:
                my_dict[str1] = [str1]
        for key in my_dict:
            print(my_dict[key])
            res.append(my_dict[key])
        return res
#Solution 2 (Sort and Mapping)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        my_dict = {}
        for s in strs:
            #리스트로 변환해버려서 이렇게 못함
            # sorted_str = sorted(s)
            # print(sorted_str)
            #정렬된 문자열로 만들기
            sorted_str = ''.join(sorted(s)) # n log n

            if sorted_str in my_dict:
                my_dict[sorted_str].append(s)
            else:
                my_dict[sorted_str] = [s]
        print(my_dict)
        for key in my_dict:
            res.append(my_dict[key])
        return res
#Solution 3
