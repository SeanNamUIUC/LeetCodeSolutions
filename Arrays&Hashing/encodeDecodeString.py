
# Encode and Decode Strings
# Solved 
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.


class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        #ex)  4#neet4#code4#love3#you
        i = 0
       
        # for loop에서는 인덱스를 제어 불가능함
        while (i < len(s)):
            #j로 문자열의 총 길이 알기
            j = i
            while(s[j] != '#'):
                j += 1
            length = int(s[i:j])
            tempStr = s[j + 1: j + 1 + length]
            res.append(tempStr)
            #누적합이 아니라 현재위치기준으로
            i = j  + 1 + length

                
        return res