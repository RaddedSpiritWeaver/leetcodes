from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root:TreeNode) -> list[int]:
    queue = []
    result = []
    if root is None:
        return result
    
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
        
    return result
        

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #   gonna go down level by level
        if len(root) == 0:
            return True

        level = 1
        while (2 ** level) - 1 <= len(root):
            #   TODO: could change the iteration
            #   take that sub array, it should be palindrome
            level_begin = 2 ** (level - 1) - 1
            level_end = 2 ** level - 1
            sublist = root[level_begin : level_end]
            if  sublist != sublist[::-1]:
                return False
            level += 1
        return True
    

if __name__ == "__main__":
    s = Solution()
    root = [1,2,2,3,4,4,3]
    print(s.isSymmetric(root))