from typing import List
"""
just going through the array and assigning the regions might not be 
the minimum, since if a ballon intersects with two regions,we will
chose the first one and it may not be the optimal approach

guess its better to add to a region where the region gets the least amount of tightening

trick is to sort by the interval start time :))

even using my older version didnt make it fast and i need to drop the n^2 thing, *my nested for
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        length = len(points)
        i = 1
        while i < length:
            #   check i and i - 1
            a, b = points[i - 1], points[i]
            # begining of i is smaller than ending of i - 1, they overlap
            if b[0] <= a[1]:
                # replace i - 1 with the overlapping section, and pop out points i
                points[i - 1] = [max(a[0], b[0]), min(a[1], b[1])]
                del points[i]
                length -= 1
            else:
                i += 1
            
        return len(points)
    
if __name__ == "__main__":
    sol = Solution()
    # points = [[10,16],[2,8],[1,6],[7,12]]
    points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    print(sol.findMinArrowShots(points=points))
    