# Definition for a binary tree node.
from typing import Optional

"""
if it was possible to have the parents, we could go to the deepest node from the root,
and set that to be our root and rebuilt the tree and just ran another dfs to get the depth
and that would have been our answer
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        visit_depths = []
        value = []
        def dfs(node: TreeNode):
            if node is None:
                return -1
            # right_depth, left_depth = 0, 0
            right_depth = 1 + dfs(node.right)
            left_depth = 1 + dfs(node.left)
            
            visit_depths.append(left_depth + right_depth)
            value.append(node.val)
            return max(right_depth, left_depth)
            
        dfs(root)
        return max(visit_depths)
            
            
    
if __name__ == "__main__":
    sol = Solution()
    # p = TreeNode(1, left=TreeNode(2,left=TreeNode(4),
    #                                 right=TreeNode(5)),
    #                 right=TreeNode(3))
    
    p = TreeNode(1, left= TreeNode(2, 
                                   left = TreeNode(4, right=TreeNode(6)),
                                   right= TreeNode(5, left= TreeNode(7, right=TreeNode(8)))),
                    right=TreeNode(3))
    
    print(sol.diameterOfBinaryTree(p))