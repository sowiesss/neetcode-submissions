# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)


    def add(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int):
        if not (l1 or l2 or carry):
            return None

        d1 = d2 = 0

        if l1:
            d1 = l1.val
        if l2:
            d2 = l2.val
        
        s = d1 + d2 + carry
        d = s % 10
        c = s // 10
        
        node = ListNode(d)
        p1 = p2 = None
        if l1:
            p1 = l1.next
        if l2:
            p2 = l2.next
        node.next = self.add(p1, p2, c)

        return node

        
