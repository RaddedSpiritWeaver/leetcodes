from typing import List

#   TODO:   can do this all in one run of the array basically
#   TODO:   add zeros support, in case there is one zero, all are zero and the zero position is the total prod
#           if there is more than 1 zero, then the entire answer is zero
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length
        
        # make postfix product and store in answer
        product = 1
        for i in range(length - 2, -1, -1):
            product *= nums[i + 1]
            ans[i] = product
        
        # now make prefix product multiply by ans
        product = 1
        for i in range(1, length):
            product *= nums[i - 1]
            ans[i] *= product
        
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    print(sol.productExceptSelf(nums))