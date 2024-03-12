# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    this time in O(N) we will just store the prefix sum up to each node and when we get the same prefix sum,
    we need to get those nodes and reconnect
    """
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefix_sums = {0 : dummy}
        
        current_sum = 0
        node = dummy.next
        while node:
            current_sum += node.val
            if current_sum not in prefix_sums:
                prefix_sums[current_sum] = node
            else:
                prev = prefix_sums[current_sum]
                prev.next = node.next
            node = node.next
            
        return dummy.next
    
    """
    kinda like method one where we n^2 search for every possible sequence and check if they sum to 0
    """    
    def removeZeroSumSublists_method1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = dummy
        
        while start:
            gathered_sum = 0
            end = start.next
            while end:
                gathered_sum += end.val
                if gathered_sum == 0:
                    start.next = end.next
                end = end.next
            
            start = start.next
        
        return dummy.next
        
    def removeZeroSumSublists_method0(self, head: Optional[ListNode]) -> Optional[ListNode]:
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