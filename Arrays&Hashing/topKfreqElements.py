
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = []
        #initialized with 0s
        my_dict = defaultdict(int) 
        for num in nums:
            my_dict[num] += 1

        #1 is most frequent , then 2
        while(k != 0):
            freq_key = 0 #initialization
            frequency = 0
            for key in my_dict:
                #update frequency
                if my_dict[key] > frequency:
                    freq_key = key
                    frequency = my_dict[key]
            #decrease k, append to result
            k -= 1
            res.append(freq_key)
            if (k == 0):
                break
            my_dict.pop(freq_key)
        
        return res