from typing import List
from collections import Counter, defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        reverse_dict = defaultdict(list)
        for key in freq.keys():
            reverse_dict[freq[key]].append(key)
        
        res = []
        for key in sorted(reverse_dict.keys()):
            #   key is the count of the elements
            vals = sorted(reverse_dict[key], reverse=True)
            for val in vals:
                for _ in range(key):
                    res.append(val)
                    
        return res        
    
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,1,-6,4,5,-6,1,4,1]
    print(sol.frequencySort(nums))