from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if ladders >= (len(heights) - 1):
            #   you can totally reach the end
            return (len(heights) - 1)
        up_down = [0 for _ in range(len(heights))]
        for i in range(1, len(heights)):
            if heights[i - 1] >= heights[i]:
                up_down[i] = 0
            else:
                up_down[i] = heights[i] - heights[i - 1]
        
        # print([(up_down[i], i) for i in range(len(up_down))])
        
        last_building = len(up_down)
        skipped = 0
        for i in range(last_building):
            cur = last_building - i
            if up_down[cur - 1] == 0 and not (cur - 1 == 0):
                skipped += 1
                continue
                    
            #   build the path heap
            path = up_down[:cur]
            heapq._heapify_max(path)
            #   see if its traversable
            for _ in range(ladders):
                heapq._heappop_max(path)
            if sum(path) <= bricks:
                return cur - 1 + skipped
            skipped = 0
    

if __name__ == "__main__":
    s = Solution()
    # heights = [4,2,7,6,9,14,12]
    # bricks = 5
    # laders = 1
    heights = [1,13,1,1,13,5,11,11]
    bricks = 10
    laders = 8
    
    
    print(s.furthestBuilding(heights, bricks, laders))