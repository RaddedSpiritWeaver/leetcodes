from typing import List
"""
just going through the array and assigning the regions might not be 
the minimum, since if a ballon intersects with two regions,we will
chose the first one and it may not be the optimal approach

guess its better to add to a region where the region gets the least amount of tightening

trick is to sort by the interval start time :))

even using my older version didnt make it fast and i need to drop the n^2 thing, *my nested for

since they are sorted, then the merged things begining is always from the current, max(beginings) = curr.begin

!!! --> trick to intervals is usually sorting
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[0])
        res = 1
        prev = points[0]
        for i in range(1, len(points)):
            cur = points[i]
            if cur[0] <= prev[1]:
                #   overlap
                prev = [cur[0], min(prev[1], cur[1])]
            else:
                res += 1
                prev = cur
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    # points = [[10,16],[2,8],[1,6],[7,12]]
    points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    print(sol.findMinArrowShots(points=points))
    