# Definition for a binary tree node.
from typing import Optional
from typing import List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        #   store the node and the depth (level) in the queue
        queue: List[Tuple[TreeNode, int]] = [(TreeNode(-1, left=root), -1)]
        level_holder = -1
        #   or 100_001
        last_value = -1
        #   use it just to decrease the mod check, basically a mirror of level_holder % 2
        next_row_even = True

        def eval_node(node:TreeNode):
            nonlocal last_value
            nonlocal next_row_even
            if next_row_even:
                if last_value >= node.val or node.val % 2 == 0:
                    return False
            else:
                if last_value <= node.val or node.val % 2 == 1:
                    return False
            last_value = node.val
            return True

        while queue:
            node, level = queue.pop(0)
            if level != level_holder:
                #   we are in a new level
                level_holder = level
                if level_holder % 2 == 1:
                    # set to minimum
                    last_value = -1
                    next_row_even = True
                else:
                    last_value = 1_000_001
                    next_row_even = False
                    
            if node.left is not None:
                queue.append((node.left, level + 1))
                if not eval_node(node.left):
                    return False
            if node.right is not None:
                queue.append((node.right, level + 1))
                if not eval_node(node.right):
                    return False
            
        return True
        
    
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1,  left= TreeNode(10, 
                                        left = TreeNode(3,left=TreeNode(12), right=TreeNode(8))),
                        right=TreeNode(4,
                                       left=TreeNode(7, left=TreeNode(6)),
                                       right=TreeNode(9, right=TreeNode(2))))
    print(sol.isEvenOddTree(root))