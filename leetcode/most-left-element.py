# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#   // always better to hold the max instead of finding it again :))
class Solution:
    max_depth = -1
    val = -1
    def dfs(self, node: TreeNode, depth:int):
            if node is None:
                return
            #   prioritize left
            self.dfs(node.left, depth + 1)
            self.dfs(node.right, depth + 1)
            #   instead of appending to the list of visited, just hold the one with max
            #   will only trigger once for each row
            if depth > self.max_depth:
                self.max_depth = depth
                self.val = node.val
            return
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.val
    
if __name__ == "__main__":
    sol = Solution()
    # root = TreeNode(0)
    root = TreeNode(1,  left=  TreeNode(2,  left= TreeNode(4)),
                        right= TreeNode(3,  left= TreeNode(5, left=TreeNode(7)),
                                            right=TreeNode(6)))
    print(sol.findBottomLeftValue(root))