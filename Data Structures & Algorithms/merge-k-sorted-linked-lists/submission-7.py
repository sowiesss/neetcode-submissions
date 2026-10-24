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

        heap = []
        
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        dummy = curr = ListNode()
        while heap:
            val, ind, top = heapq.heappop(heap)
            curr.next = top
            if top.next:
                heapq.heappush(heap, (top.next.val, ind, top.next))  
            curr = curr.next
        
        return dummy.next
