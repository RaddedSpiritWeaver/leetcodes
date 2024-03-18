from typing import List

"""
just going through the array and assigning the regions might not be 
the minimum, since if a ballon intersects with two regions,we will
chose the first one and it may not be the optimal approach
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #   need to first handle the smallest balloons since they would probably not intersect
        points.sort(key=lambda x: (x[1] - x[0]))
        areas = []
        for point in points:
            for region in areas:
                #   if intersect, then merge
                if point[1] < region[0] or region[1] < point[0]:
                    continue
                else:
                    region[0] = max(point[0], region[0])
                    region[1] = min(region[1], point[1])
                    break
            else:
                areas.append(point)
        
        return len(areas)
    
if __name__ == "__main__":
    sol = Solution()
    points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    print(sol.findMinArrowShots(points=points))
    