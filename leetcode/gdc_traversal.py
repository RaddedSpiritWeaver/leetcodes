from typing import List
from collections import Counter
import math

#   answer is false if there are two numbers that are indivisible to each other, like 3 and 5, and have no
#   other common multiplicand

#   inspired by https://www.youtube.com/watch?v=0jNmHPfA_yE&t=466s

class Node:
    def __init__(self, parent):
        self.parent = parent
        pass


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        #   initially everyone is in their own group
        group = [i for i in range(len(nums))]

        def get_root(index):
            while group[index] != index:
                index = group[index]
            return index

        def join(i, j):
            #   get i parent root
            index = group[i]
            root_i = get_root(i)
            root_j = get_root(j)
            #   point root of j to i root
            group[root_j] = group[root_i]

        for i in range(len(nums)):
            for j in range(i):
                if math.gcd(nums[i], nums[j]) > 1:
                    #   need to join their roots
                    join(i,j)
                    
        #   if everything is in the same group then we return true
        roots = []
        for i in range(len(group)):
            roots.append(get_root(i))
            
        if len(Counter(roots)) == 1:
            return True

        return False
        
        
        
if __name__ == "__main__":
    sol = Solution()
    nums = [3,5,9]
    print(sol.canTraverseAllPairs(nums))