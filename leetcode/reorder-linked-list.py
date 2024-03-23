from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        stack = []
        while fast and fast.next:
            stack.append(slow)
            slow = slow.next
            fast = fast.next.next
            
        #   if termination condition was that fast.next is null, then its an odd length list
        #   and the slow pointer in on the middle node, so we must push it once before stacking the remainder
        build = None
        if fast:
            tmp = slow.next
            build = slow
            build.next = None
            slow = tmp
            
       #    in the first iteration build is either none and the end, or a node that is the last node (node->none)
        while slow:
            before = stack.pop()
            before.next = slow
            tmp = slow.next
            slow.next = build
            build = before
            slow = tmp

        return head
    
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = sol.reorderList(head)
    while res:
        print(res.val)
        res = res.next