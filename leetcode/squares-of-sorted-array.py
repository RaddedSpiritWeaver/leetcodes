from typing import List

"""
well obviously we can just square everything and then sort
but we wanna try it in O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        stack = []
        for num in nums:
            squared = num ** 2
            if num < 0:
                stack.append(squared)
            else:
                while stack:
                    if stack[-1] <= squared:
                        res.append(stack.pop())
                    else: break
                res.append(squared)
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [-7,-3,2,3,11]
    print(sol.sortedSquares(nums))