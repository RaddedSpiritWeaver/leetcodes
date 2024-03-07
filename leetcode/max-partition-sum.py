from typing import List
import heapq
"""
in a dp way, we should first solve it form k = 1 and then build up to the actual k

select the min values and merge them with their highest neighbor
"""

class GroupNode:
    def __init__(self, value, range):
        self.value = value
        self.range = range
        self.right = None
        self.left = None

# mostleft = left = GroupNode(arr[0], (0, 1))
#         for i in range(1,len(arr)):
#             right = GroupNode(arr[i], (i, i+1))
#             left.right = right
#             right.left = left
#             left = right
#         pass


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
                groups[smallest_val_index] = group
                arr[smallest_val_index] = left_val
                heapq.heappush(heap, left_val)
                return True
            return False
        
        for kk in range(2, k + 1):
            go_next = False
            while heap and not go_next:
                smallest_val = heapq.heappop(heap)
                indices = [i for i in range(len(arr)) if arr[i] == smallest_val]
                for smallest_val_index in indices:
                    #   check its left and right values
                    left = smallest_val_index - 1
                    right = smallest_val_index + 1
                    left_val = arr[left] if left >= 0 else -1
                    right_val = arr[right] if right < len(arr) else -1
                    cur_group = groups[smallest_val_index]
                    #   prioritize left
                    if left_val >= right_val:
                        #   left
                        #   check the group
                        group = groups[left]
                        if group != cur_group and groups.count(group) < kk:
                            #   merge
                            groups[smallest_val_index] = group
                            arr[smallest_val_index] = left_val
                            heapq.heappush(heap, left_val)
                            continue
                        group = groups[right]
                        if group != cur_group and groups.count(group) < kk:
                            #   merge
                            groups[smallest_val_index] = group
                            arr[smallest_val_index] = right_val
                            heapq.heappush(heap, right_val)
                            continue
                    else:
                        group = groups[right]
                        if group != cur_group and groups.count(group) < kk:
                            #   merge
                            groups[smallest_val_index] = group
                            arr[smallest_val_index] = right_val
                            heapq.heappush(heap, right_val)
                            continue
                        group = groups[left]
                        if group != cur_group and groups.count(group) < kk:
                            #   merge
                            groups[smallest_val_index] = group
                            arr[smallest_val_index] = left_val
                            heapq.heappush(heap, left_val)
                            continue
                
                heapq.heappush(heap, smallest_val)
                go_next = True
                
                
                
        print(arr)
        return sum(arr)
        
        
    
if __name__ == "__main__":
    sol = Solution()
    arr = [1,15,7,9,2,5,10]
    k = 3
    print(sol.maxSumAfterPartitioning(arr, k))
    
    
"""
[1,15,7,9,2,5,10]
[1,2,3,4,5,6,7]
[15,15,7,10,10,4,10,10,4]
[15,15,15,10,19,10]
"""