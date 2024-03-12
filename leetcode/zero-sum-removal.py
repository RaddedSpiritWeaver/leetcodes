# Definition for singly-linked list.

from typing import Optional

"""
[1,1,4,-2,-3,5,-5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # convert to list
        node = head
        l = []
        while node:
            l.append(node.val)
            node = node.next

        back = 0
        length = len(l)
        remove_ranges = []
        while back < length:
            for i in range(back + 1, length + 1):
                if sum(l[back:i]) == 0:
                    #   remove this section of the list
                    remove_ranges.append((back, i))
                    back = i
            back += 1
        remove_ranges.sort(reverse=True, key=lambda x:x[0])
        for r in remove_ranges:
            del l[r[0]:r[1]]
        
        # convert back to linked list
        if l:
            prev = head = ListNode(l[0])
            for i in range(1,len(l)):
                node = ListNode(l[i])
                prev.next = node
                prev = node
            
            return head
        else:
            return None
        
        
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))
    head = sol.removeZeroSumSublists(head)
    
    node = head
    l = []
    while node:
        l.append(node.val)
        node = node.next
    print(l)