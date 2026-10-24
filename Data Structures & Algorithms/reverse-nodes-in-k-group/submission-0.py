# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = head

        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
            

        nexth = curr
        curr = head
        prev = self.reverseKGroup(nexth, k)

        while curr != nexth:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n

        return prev
        



