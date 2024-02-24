from typing import List, Dict, Set

# TODO: we can do only one for on the sorted meetings based on time, and hold meetings form a certain time stamp
# and if we get a known person, we will update all the meetings in that time frame

# class Node:
#     def __init__(self,label:int, rank:int):
#         self.label = label
#         self.rank = rank
#         self.children = []
        
#     def add_child()

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knows = [False for _ in range(n)]
        knows[0] = True
        knows[firstPerson] = True
        #   stores the min time knoews
        time_knew = [100_001 for _ in range(n)]
        time_knew[0] = 0
        time_knew[firstPerson] = 0
        
        rels = [[] for _ in range(n)]
        
        # meetings.sort(key= lambda x: x[2])
        for p1, p2, t in meetings:
            rels[p1].append([p2, t])
            rels[p2].append([p1, t])
            
        def handle(person_index):
            #   iterate over its relations
            p_rels = rels[person_index]
            #   mark relations that have a knowing time after the event
            marked_indecies = []
            for i in range(len(p_rels)):
                #   time of meeting before knowledge
                if p_rels[i][1] < time_knew[person_index]:
                    continue
                
                knows[p_rels[i][0]] = True
                
                if time_knew[p_rels[i][0]] > p_rels[i][1]:
                    time_knew[p_rels[i][0]] = p_rels[i][1]
                    marked_indecies.append(i)
                    #   update the child again
            for i in sorted(marked_indecies, reverse=True):
                child = p_rels[i][0]
                del p_rels[i]
                handle(child)
                
        for i in range(n):
            if knows[i]:
                handle(i)
                
        return [x for x in range(len(knows)) if knows[x]]
            
    
if __name__ == "__main__":
    s = Solution()
    n = 6
    meetings = [[1,2,5],[2,3,8],[1,5,10]]
    first_person = 1
    print(s.findAllPeople(n, meetings, first_person))