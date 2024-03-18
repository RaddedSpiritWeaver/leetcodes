from typing import List
"""
just going through the array and assigning the regions might not be 
the minimum, since if a ballon intersects with two regions,we will
chose the first one and it may not be the optimal approach

guess its better to add to a region where the region gets the least amount of tightening
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #   need to first handle the smallest balloons since they would probably not intersect
        points.sort(key=lambda x: (x[1] - x[0]))
        areas = []
        for point in points:
            matches = []
            for i, region in enumerate(areas):
                #   if intersect, then merge
                if point[1] < region[0] or region[1] < point[0]:
                    continue
                else:
                    new_region = [max(point[0], region[0]), min(region[1], point[1])]
                    diff = region[1] - region[0] - new_region[1] + new_region[0]
                    matches.append((i, new_region, diff)) 
            if matches:
                #   get the min diff match and change that
                min_match = min(matches, key=lambda x: x[2])
                region = areas[min_match[0]]
                region[0] = min_match[1][0]
                region[1] = min_match[1][1]
            else:
                areas.append(point)
            # areas.sort(key=lambda x: (x[1] - x[0]))
                
        return len(areas)
    
if __name__ == "__main__":
    sol = Solution()
    points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    print(sol.findMinArrowShots(points=points))
    