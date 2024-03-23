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
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        #   if termination condition was that fast.next is null, then its an odd length list
        #   and the slow pointer in on the middle node, so we must push it once before stacking the remainder
        if fast:
            slow = slow.next

        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next

        print(stack)
        node = head
        end = node
        while node != middle and stack:
            last = stack.pop()
            next_node = node.next
            node.next = last
            last.next = next_node
            end = last
            node = next_node
        
        if fast:
            end.next = middle
        middle.next = None

        return head
    
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(sol.reorderList(head))