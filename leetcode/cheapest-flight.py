#   we are going to go with graph representation
#   storing the incoming and out going paths from each node, some redundancy
#   then we will perform a UCS with a depth limit to see if we can find the least cost path
#   going to need heapq for this

import heapq
from typing import List

#   format of child and parent: (label, cost)
class Node:
    def __init__(self, label) -> None:
        self.label = label
        #   only used for faster reply for path finding
        self.parents = []   
        self.children = []
        pass
    
    def add_child(self, child_index, cost):
        self.children.append((child_index, cost))
        
    def add_parent(self, p_index, cost):
        self.parents.append((p_index, cost))
    
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #   first create N nodes, label and index would be the same
        nodes = [Node(i) for i in range(n)]
        
        #   create the graph
        for frm, to, cost in flights:
            nodes[frm].add_child(to, cost)
            nodes[to].add_parent(frm, cost)
            
        #   check if source has out going paths, and if dst has incoming paths
        #   there would be no way to solve the question
        if len(nodes[src].children) == 0 or len(nodes[dst].parents) == 0:
            return -1
        
        #   ok now the search begins
        #   need to have a heapq storing (current_cost, node_index, depth)
        visited = []
        queue = [(0, src, 0)]
        result = -1
        #   while there is an element in the queue
        while queue:
            node = heapq.heappop(queue)
            #   depth check
            if node[2] > (k + 1):
                continue
            
            #   check for termination
            if node[1] == dst:
                result = node[0]
                break
            
            #   visited check
            # if node[1] in visited:
            #     continue
            
            #   all tests passed, add to visited and process
            # visited.append(node[1])
            #   child expansion
            for child_index, cost in nodes[node[1]].children:
                new_element = (node[0] + cost, child_index, node[2] + 1)
                heapq.heappush(queue, new_element)
                
        return result           
    
if __name__ == "__main__":
    s = Solution()
    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    print(s.findCheapestPrice(n, flights, src, dst, k))