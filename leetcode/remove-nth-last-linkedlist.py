# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    the most obvious way is to get to the end so we know the len,
    and then come to it
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = {}
        length = 0
        node = head
        while node is not None:
            nodes[length] = node
            length += 1
            node = node.next
            
        target = length - n
        before, after = None, None
        if target - 1 >= 0:
            before = nodes[target - 1]
        
        if target + 1 < length:
            after = nodes[target + 1]
        
        if before is None:
            if after is None:
                return None
            else:
                return after
        else:
            before.next = after
        
        return head
    
if __name__ == "__main__":
    sol = Solution()
    l = [1,2,3,4,5]
    n = 1
    head = ListNode(1)
    last = head
    for i in range(1, len(l)):
        new = ListNode(val=l[i])
        last.next = new
        last = new
    head = sol.removeNthFromEnd(head, n)
    res = []
    while head is not None:
        res.append(head.val)
        head = head.next
    print(res)