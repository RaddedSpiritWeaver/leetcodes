from typing import List
import heapq
"""
in a dp way, we should first solve it form k = 1 and then build up to the actual k

select the min values and merge them with their highest neighbor
"""

"""
wanted to be clever and not brute force it but in the end, lets just go for an actual brute force thing,
so in my original thoughts about brute forcing this issue, i had the idea to make it like a search thing and generate
next states based on the current state, but i cant figure a nice way to code this at all :)

now after cheating a bit we are going to go for a recursive construction of the method
start from the beginning of the array, and then imagine all possible sub sets this contains
and then call the function from that point on
"""

class Solution:
    
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        #   handle extremes
        if k == 1:
            return sum(arr)
        
        if k == len(arr):
            return len(arr) * max(arr)
        
        # results = []
        max_holder = 0
        arr_len = len(arr)
        
        def sub_partition(current_state:list, start):
            nonlocal max_holder
            for kk in range(1,k + 1):
                if start + kk <= arr_len:
                    max_val = max(arr[start:start + kk])
                    current_state[start:start + kk] = [max_val] * kk
                    if arr[start:start + kk] == [2,5,10]:
                        pass
                    if sum(current_state) > max_holder:
                        max_holder = sum(current_state)
                    sub_partition(current_state.copy(),start + kk)
            return
        
        sub_partition(arr.copy(), 0)
        # for r in results:
        #     print(r)
        
        # print("!!!-!!!-!!!-!!!")
        # x = max(results, key=sum)
        return max_holder
        
    
if __name__ == "__main__":
    sol = Solution()
    # arr = [1,4,1,5,7,3,6,1,9,9,3]
    # k = 4
    arr = [1,15,7,9,2,5,10]
    k = 3
    print(sol.maxSumAfterPartitioning(arr, k))
    
    
"""
[1,15,7,9,2,5,10]
[0,1,2,3,4,5,6]
[1,2,3,4,5,6,7]
[15,15,7,10,10,4,10,10,4]
[15,15,15,10,19,10]
"""