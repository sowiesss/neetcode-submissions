# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k < 1:
            return None

        for i in range(1, k):
           lists[i] = self.merge2Lists(lists[i - 1], lists[i])
        
        return lists[-1]


    def merge2Lists(self, l1: Optional[ListNode], l2: Optional[ListNode])-> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = curr = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        
        curr.next = l1 or l2

        return dummy.next
