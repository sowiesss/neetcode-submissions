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
        if k == 1:
            return lists[0]

        mergedLists = []
        i = 0
        while i < k - 1:
            mergeh = self.merge2Lists(lists[i], lists[i + 1])
            if mergeh:
                mergedLists.append(mergeh)
            i += 2
        
        if k % 2:
            mergedLists.append(lists[i])

        return self.mergeKLists(mergedLists)


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
            # print(curr.val)
        
        curr.next = l1 or l2

        return dummy.next
