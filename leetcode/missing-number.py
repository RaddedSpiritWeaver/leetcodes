import heapq
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        index = 0
        while nums:
            num = heapq.heappop(nums)
            if num != index:
                return index
            index += 1
        return index

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         index = 0
#         for i in range(len(nums) + 1):
#             if index == len(nums):
#                 return index
#             if index != nums[i]:
#                 return index
#             index += 1
            
if __name__ == "__main__":
    s = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print(Solution.missingNumber(nums))