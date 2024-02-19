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

def dfs(node: TreeNode):
    if node.left is not None:
        dfs(node.left)
    if node.right is not None:
        dfs(node.right)
    return node.val

def get_most_deep(node: TreeNode, left= True):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return node.val
    if left:
        return get_most_deep(node.left)
    else:
        return get_most_deep(node.right)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        print(dfs(root))
        return "im passing"
    

if __name__ == "__main__":
    s = Solution()
    # root = [1,2,2,3,4,4,3]
    root = TreeNode(val= 1, 
                    left= TreeNode(val= 2,
                                   left= TreeNode(val= 3, left= None, right= None),
                                   right= TreeNode(val= 4, left= None, right= None),),
                    
                    right= TreeNode(val= 2,
                                    left= TreeNode(val= 4, left= None, right= None),
                                    right= TreeNode(val= 3, left= None, right= None))
                    )
    print(get_most_deep(root))
    print(get_most_deep(root.right, False))
    # root = TreeNode(val= 1, 
    #                 left= TreeNode(val= 2,
    #                                left= None,
    #                                right= TreeNode(val= 3, left= None, right= None),),
                    
    #                 right= TreeNode(val= 2,
    #                                 left= None,
    #                                 right= TreeNode(val= 3, left= None, right= None))
    #                 )
    
    # print(s.isSymmetric(root))