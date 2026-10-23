# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: return None

        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if not fast: # end of the list
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head
