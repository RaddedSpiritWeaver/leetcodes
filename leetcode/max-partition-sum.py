from typing import List
import heapq
"""
in a dp way, we should first solve it form k = 1 and then build up to the actual k

select the min values and merge them with their highest neighbor
"""
class Solution:
    
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if k == 1:
            return sum(arr)
        
        heap = arr.copy()
        heapq.heapify(heap)
        groups = [i for i in range(1,len(arr) + 1)]
        
        def check_and_merge(target, target_val, small_index, small_group):
            group = groups[target]
            if group != small_group and groups.count(group) < kk:
                #   merge
                groups[small_index] = group
                arr[small_index] = target_val
                heapq.heappush(heap, target_val)
                return True
            return False
        
        for kk in range(2, k + 1):
            go_next = False
            processed = [False] * len(arr)
            while heap and not go_next:
                smallest_val = heapq.heappop(heap)
                indices = [i for i in range(len(arr)) if arr[i] == smallest_val]
                for smallest_val_index in indices:
                    #   check its left and right values
                    processed[smallest_val_index] = True
                    left = smallest_val_index - 1
                    right = smallest_val_index + 1
                    left_val = arr[left] if left >= 0 else -1
                    right_val = arr[right] if right < len(arr) else -1
                    cur_group = groups[smallest_val_index]
                    #   prioritize left
                    if left_val >= right_val:
                        #   left
                        if check_and_merge(left, left_val, smallest_val_index, cur_group): break
                        elif check_and_merge(right, right_val, smallest_val_index, cur_group): break
                        else: 
                            heapq.heappush(heap, smallest_val)
                            go_next = True
                    else:
                        #   right
                        if check_and_merge(right, right_val, smallest_val_index, cur_group): break
                        elif check_and_merge(left, left_val, smallest_val_index, cur_group): break
                        else: 
                            heapq.heappush(heap, smallest_val)
                            go_next = True
                # else:
                #     go_next = True
                
                
                
        print(arr)
        return sum(arr)
        
        
    
if __name__ == "__main__":
    sol = Solution()
    # arr = [1,4,1,5,7,3,6,1,9,9,3]
    # k = 4
    arr = [1,15,7,9,2,5,10]
    k = 3
    print(sol.maxSumAfterPartitioning(arr, k))
    
    
"""
[1,15,7,9,2,5,10]
[1,2,3,4,5,6,7]
[15,15,7,10,10,4,10,10,4]
[15,15,15,10,19,10]
"""