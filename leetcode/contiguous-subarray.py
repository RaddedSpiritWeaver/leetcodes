from typing import List
from collections import defaultdict

#   TODO: we can be more efficient if we update the max distance while we are adding new entries to the map
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        indices[0] = [-1]
        pfs = 0
        for i, num in enumerate(nums):
            if num:
                pfs += 1
            else:
                pfs -= 1
            indices[pfs].append(i)
        
        # go through the keys
        max_dist = 0
        for l in indices.values():
            begin, end = l[0], l[-1]
            if begin != end:
                dist = end - begin
                if dist > max_dist:
                    max_dist = dist
                
        return max_dist
            
            
            
if __name__ == "__main__":
    sol = Solution()
    # nums = [0,1]
    nums  = [1,1,1,0,0,0]
    print(sol.findMaxLength(nums))