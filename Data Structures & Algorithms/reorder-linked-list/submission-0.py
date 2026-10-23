# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        nxt = slow.next
        prev = slow.next = None
        
        while nxt:
            temp = nxt.next
            nxt.next = prev
            prev = nxt
            nxt = temp
        
        l, r = head, prev
        while r:
            t1, t2 = l.next, r.next
            l.next = r
            r.next = t1
            l, r = t1, t2



