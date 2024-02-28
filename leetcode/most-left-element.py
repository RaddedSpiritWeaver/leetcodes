# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        #   lets make a dfs traversal prioritizing left
        #   with this traversal, also get depth of the tree
        #   store the left visits with their depth
        #   in the end return the first node with the most depth from the left side visits
        left_visits = []
        
        def dfs(node: TreeNode, depth:int, is_left=False):
            if node is None:
                return depth - 1
            #   prioritize left
            l_d = dfs(node.left, depth + 1, True)
            r_d = dfs(node.right, depth + 1)
            
            if is_left:
                left_visits.append((node.val, depth))
            return max(l_d, r_d)
        
        max_depth = dfs(root)
        
        for left_leaf in left_visits:
            if left_leaf[1] == max_depth:
                return left_leaf[0]
            
        #   there might be a problem for just a root, or maybe there might be cases where left most node in the last row is a right child
        #   and i understood the question wrong
    
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1,  left=  TreeNode(2,  left= TreeNode(4)),
                        right= TreeNode(3,  left= TreeNode(5, left=TreeNode(7)),
                                            right=TreeNode(6)))
    print(sol.findBottomLeftValue(root))