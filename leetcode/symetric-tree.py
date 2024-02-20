from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#   wouldnt work since if there is cut in the branches we need to add a lot of extra logic to make it fill those empty
#   slots with none and its gets messy, and need to use the node child method indexing thing
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
            continue
        else:
            result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
        
    return result
        

# def get_child(index: int, left = True):
#     if left:
#         return 2 * index + 1
#     else:
#         return 2 * index + 2

def dfs(node: TreeNode, visits_right:list, visits_left:list):
    if node.left is not None:
        x = dfs(node.left, visits_right, visits_left)
        visits_left.append(x)
    if node.right is not None:
        x = dfs(node.right, visits_right, visits_left)
        visits_right.append(x)
    print(node.val)
    return node.val

def dfs_a(node: TreeNode, traversal:list):
    if node is None:
        print("None")
        traversal.append(None)
        return
    print(node.val)
    traversal.append(node.val)
    if node.left is None and node.right is None:
        return
    if node.left is not None:
        dfs_a(node.left, traversal)
    if node.right is not None:
        dfs_a(node.right, traversal)
        
    
def dfs_b(node:TreeNode, visits:list, left= True):
    if node is None: 
            visits.append("None")
            return
    if left:
        dfs_b(node.left, visits)
        dfs_b(node.right, visits)
        visits.append(node.val)
        return
    else:
        dfs_b(node.right, visits, False)
        dfs_b(node.left, visits, False)
        visits.append(node.val)
        return
    

def dfs_change_able(node:TreeNode, visits:list, left= True):
    if left:
        if node.left is not None:
            dfs_change_able(node.left, visits)
        if node.right is not None:
            dfs_change_able(node.right, visits)
        visits.append(node.val)
        return
    else:
        if node.right is not None:
            dfs_change_able(node.right, visits)
        if node.left is not None:
            dfs_change_able(node.left, visits)
        visits.append(node.val)
        return

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
        overall_visits = []
        visits_left, visits_right = [], []
        # print(dfs(root, visits_right, visits_left))
        dfs_change_able(root.left, visits_left)
        dfs_change_able(root.right, visits_right, left=False)
        return "im passing"
    

if __name__ == "__main__":
    s = Solution()
    # root = [1,2,2,3,4,4,3]
    root = TreeNode(val= 1, 
                    left= TreeNode(val= 2,
                                   left= TreeNode(val= 3, left= None, right= None),
                                   right= TreeNode(val= 4, left= TreeNode(val=5, left=None, right=None), right= None),),
                    
                    right= TreeNode(val= 2,
                                    left= TreeNode(val= 4, left= None, right= TreeNode(val=5, left=None, right=None)),
                                    right= TreeNode(val= 3, left= None, right= None))
                    )
    
    root = TreeNode(val=1, right= None, left=None)
    
    # root = TreeNode(val= 1, 
    #                 left= TreeNode(val= 2,
    #                                left= None,
    #                                right= TreeNode(val= 3, left= None, right= None),),
                    
    #                 right= TreeNode(val= 2,
    #                                 left= None,
    #                                 right= TreeNode(val= 3, left= None, right= None))
    #                 )
    # l = []
    # l1 = []
    # l2 = []
    # dfs_a(root, l)
    # dfs_a(root.left, l1)
    # dfs_a(root.right, l2)
    # print(l)
    # print(f"l1: {l1}")
    # print(f"l2: {l2}")
    l1, l2 = [], []
    dfs_b(root.right, l2, False)
    dfs_b(root.left, l1)
    print(l1)
    print(l2)
    
    # print(get_most_deep(root))
    # print(get_most_deep(root.right, False))
    # print(bfs(root))
    
    # print(s.isSymmetric(root))