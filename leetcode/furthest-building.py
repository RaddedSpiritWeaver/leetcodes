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
        
        last_building = len(up_down) 
        for i in range(last_building):
            cur = last_building - i
            #   build the path heap
            path = up_down[:cur]
            heapq._heapify_max(path)
            #   see if its traversable
            lads = ladders
            available_bricks = bricks
            for _ in range(ladders):
                heapq._heappop_max(path)
            if sum(path) <= bricks:
                return cur - 1
    

if __name__ == "__main__":
    s = Solution()
    heights = [4,2,7,6,9,14,12]
    bricks = 5
    laders = 1
    
    print(s.furthestBuilding(heights, bricks, laders))