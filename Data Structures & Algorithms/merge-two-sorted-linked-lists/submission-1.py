# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        p1 = list1
        p2 = list2
        new_l = ListNode()
        curr = new_l

        while p1 and p2:
            if p1.val < p2.val:
                curr.val = p1.val
                p1 = p1.next
            else:
                curr.val = p2.val
                p2 = p2.next
            curr.next = ListNode()
            curr = curr.next

        source = None
        if p1:
            source = p1
        else:
            source = p2
        
        while source.next:
            curr.val = source.val
            source = source.next
            curr.next = ListNode()
            curr = curr.next
        curr.val = source.val

        return new_l




        