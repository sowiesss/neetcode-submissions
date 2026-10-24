# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]

        return self.divide(lists, 0, k - 1)

    
    def divide(self, lists, left, right):
        if left == right:
            return lists[left]
        if left > right:
            return None
        
        mid = (left + right) // 2
        left = self.divide(lists, left, mid)
        right = self.divide(lists, mid + 1, right)

        return self.conquer(lists, left, right)

    
    def conquer(self, lists, left, right):

        dummy = curr = ListNode()

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        curr.next = left or right

        return dummy.next
        