# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
if __name__ == "__main__":
    sol = Solution()
    nodes = {
        1: ListNode(3),
        2: ListNode(2),
        3: ListNode(0),
        4: ListNode(-4),
    }
    nodes[4].next = nodes[2]
    for i in range(1,4):
        nodes[i].next = nodes[i + 1]
    
    print(sol.hasCycle(nodes[1]))