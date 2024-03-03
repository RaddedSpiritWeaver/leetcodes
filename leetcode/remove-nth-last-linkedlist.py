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
        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next
        
        i, target = 0, length - n
        node = head
        last = None
        while i != target:
            i += 1
            last = node
            node = node.next
        else:
            if last is None and node is None:
                return None
            if last is None and node is not None:
                return node.next
            last.next = node.next
        
        return head
    
    
if __name__ == "__main__":
    sol = Solution()
    l = [1,2,3,4,5]
    n = 5
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