from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def get_child(index: int, left = True):
#     if left:
#         return 2 * index + 1
#     else:
#         return 2 * index + 2




class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #   gonna go down level by level
        if len(root) == 0:
            return True

        level = 1
        while (2 ** level) - 1 <= len(root):
            #   TODO: could change the iteration
            #   take that sub array, it should be polindrom
            level_begin = 2 ** (level - 1)
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