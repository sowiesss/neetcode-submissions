# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = gh = head
        tail = newh = None
        flag = True
        while True:
            for _ in range(k):
                if not curr:
                    flag = False
                    break # group < k
                curr = curr.next
            if not flag:
                break
            
            nexth = prev = curr
            curr = gh

            while curr != nexth:
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n

            if tail:
                tail.next = prev
            else:
                newh = prev
            tail = gh
            curr = gh = nexth
            
        return newh
        



