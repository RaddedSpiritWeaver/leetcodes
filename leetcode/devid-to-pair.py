from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for key in c.keys():
            if c[key] % 2 == 1:
                return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    # nums = [2,3,3,2,2,2]
    print(sol.divideArray(nums))