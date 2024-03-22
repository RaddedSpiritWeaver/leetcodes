from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        
        print(stack)
        #   since its a one element list
        if fast == slow:
            return True
        #   if fast.next was none and the termination condition, we have an odd length list
        #   so if fast is not None, we need to pop one of the stack and then check
        if fast:
            print("poped")
            stack.pop()

        while slow:
            cur = stack.pop()
            if cur != slow.val: return False
            slow = slow.next

        return True
    
if __name__ == "__main__":
    sol = Solution()
    # head = ListNode(1, ListNode(0, ListNode(0)))
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(sol.isPalindrome(head))