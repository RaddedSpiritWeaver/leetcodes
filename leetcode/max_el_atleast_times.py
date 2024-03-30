from collections import defaultdict
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        max_val = max(nums)
        count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == max_val:
                count += 1
            while count == k:
                if nums[left] == max_val:
                    count -= 1
                left += 1
            
            if count == k - 1:
                res += left
        return res
    
if __name__ == "__main__":
    sol = Solution()
    nums = [61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82]
          #[00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    k = 2
    print(sol.countSubarrays(nums, k))