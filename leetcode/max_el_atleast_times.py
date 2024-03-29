from collections import defaultdict
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        lenn = len(nums)
        #   i know we can do Counter and max, but wanna show the overall way of the algorithim
        # max_el = max(nums)
        max_el = 0
        freq = defaultdict(int)
        for x in nums:
            if x > max_el:
                max_el = x
            freq[x] += 1
        
        if freq[max_el] < k:
            return 0

        res = 0
        initial_freq = defaultdict(int)
        for i in range(k - 1):
            initial_freq[nums[i]] += 1
        #   do a sliding window for each possible frequency more than k
        for kk in range(k, freq[max_el] + 1):
            left, right = -1, kk - 1
            #   add the new right element
            iter_counter = initial_freq.copy()
            initial_freq[nums[right]] += 1
            
            while right < lenn:
                iter_counter[nums[right]] += 1
                while iter_counter[max_el] == kk:
                    left += 1
                    iter_counter[nums[left]] -= 1
                    print(left, right, kk)
                    res += 1
                if nums[left] == max_el:
                    # move one back and one right
                    iter_counter[nums[left]] += 1
                    left -= 1
                right += 1
            
        return res
    
if __name__ == "__main__":
    sol = Solution()
    nums = [61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82]
          #[00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    k = 2
    print(sol.countSubarrays(nums, k))