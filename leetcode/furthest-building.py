from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        up_down = [0 for _ in range(len(heights))]
        for i in range(1, len(heights)):
            if heights[i - 1] >= heights[i]:
                up_down[i] = 0
            else:
                up_down[i] = heights[i] - heights[i - 1]

        path_heap = []
        used_bricks = 0
        index = 0
        while index < len(up_down):
            if up_down[index] == 0:
                index += 1
                continue
            if len(path_heap) < ladders:
                heapq.heappush(path_heap, up_down[index])
            else:
                smallest = heapq.heappushpop(path_heap, up_down[index])
                used_bricks = used_bricks + smallest
                
            if used_bricks > bricks:
                break
            
            index += 1
        
        return index - 1
    

if __name__ == "__main__":
    s = Solution()
    heights = [4,2,7,6,9,14,12]
    bricks = 5
    ladders = 1
    
    print(s.furthestBuilding(heights, bricks, ladders))