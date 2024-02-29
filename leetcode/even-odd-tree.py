# Definition for a binary tree node.
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        #   we are going to bfs with two queues, one for even, one for odd
        #   since we start at level 0
        #   TODO: think off a way to do it linear
        #   TODO: maybe also a list comprehension thing for the row checking
        even_q = [root]
        odd_q : List[TreeNode] = []
        processing_even = True
        #   TODO: for the last level, the row processing is repeated, room for efficiency
        while even_q or odd_q:
            
            
                
            if even_q and processing_even:
                node = even_q.pop(0)
                if node.left is not None:
                    odd_q.append(node.left)
                if node.right is not None:
                    odd_q.append(node.right)
                if not even_q:
                    processing_even = False
                    #   process the odd level
                    last_val = 100_000
                    for i in range(len(odd_q)):
                        if odd_q[i].val % 2 != 0 or odd_q[i].val >= last_val:
                            return False
                        last_val = odd_q[i].val
            
            if odd_q and not processing_even:
                node = odd_q.pop(0)
                if node.left is not None:
                    even_q.append(node.left)
                if node.right is not None:
                    even_q.append(node.right)
                if not odd_q:
                    processing_even = True
                    #   process the even level
                    last_val = -1
                    for i in range(len(even_q)):
                        if even_q[i].val % 2 != 1 or even_q[i].val <= last_val:
                            return False
                        last_val = even_q[i].val
        
        return True
        
    
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1,  left= TreeNode(10, 
                                        left = TreeNode(3,left=TreeNode(12), right=TreeNode(8))),
                        right=TreeNode(4,
                                       left=TreeNode(7, left=TreeNode(6)),
                                       right=TreeNode(9, right=TreeNode(2))))
    print(sol.isEvenOddTree(root))