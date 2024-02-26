# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree_1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, visited:list):
            if node is None:
                visited.append("N")
                return
            dfs(node.right, visited)
            dfs(node.left, visited)
            visited.append(node.val)
            return
        
        visit_q ,visit_p = [], []
        dfs(q, visit_q)
        dfs(p, visit_p)
        return visit_q == visit_p
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True
        
        if (p is None and q) or (p and q is None):
            return False
        
        if p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
        
        return False
    
if __name__ == "__main__":
    sol = Solution()
    p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    # q = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    
    q = TreeNode(1, left=TreeNode(3), right=TreeNode(2))
    
    print(sol.isSameTree(p, q))