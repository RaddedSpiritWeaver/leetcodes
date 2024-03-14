from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #   prefix sum counter
        #   initialize 0 with 1 we imagine there is one zero begin everything
        pfs = {0:1}
        current_sum = 0
        for num in nums:
            current_sum += num
            try:
                pfs[current_sum] += 1
            except KeyError:
                pfs[current_sum] = 1
        
        #   now max key value, max prefix sum is current sum
        result = 0
        if goal == 0:
            #   for each key, calculate arithmetic sum
            for i in range(current_sum - goal + 1):
                key_val = pfs[i]
                val = (key_val - 1) * (key_val) // 2
                result += val
        else:
            for i in range(current_sum - goal + 1):
                val = pfs[i] * pfs[i + goal]
                result += val
        return result
        
        
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,0,0,1,0,1]
    # nums = [1,0,1,0,1]
    # nums = [0,0,0,0,0]
    goal = 0
    print(sol.numSubarraysWithSum(nums=nums, goal=goal))