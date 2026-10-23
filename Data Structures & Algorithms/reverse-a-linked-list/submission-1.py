# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = ListNode()
        if head:
            prev.val = head.val
        else:
            return None
        while curr.next:
            temp = ListNode()
            temp.val = curr.next.val
            curr = curr.next
            temp.next = prev
            prev = temp

        return prev