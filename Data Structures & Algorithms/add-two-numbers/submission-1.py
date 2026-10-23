# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = newh = ListNode()
        carry = 0
        prev = None
        while l1 and l2:
            s = l1.val + l2.val + carry
            curr.val = s % 10
            carry = s // 10
            l1 = l1.next
            l2 = l2.next
            curr.next = ListNode()
            prev = curr
            curr = curr.next

        rest = None
        if l1:
            rest = l1
            print("l1")
        elif l2:
            rest = l2
            print(l2)
        elif carry:
            curr.val = carry
            return newh
         
        while rest:
            s = rest.val + carry
            curr.val = s % 10
            carry = s // 10
            curr.next = ListNode()
            prev = curr
            curr = curr.next
            rest = rest.next
        
        if carry:
            curr.val = carry
        else:
            prev.next = None

        return newh
        


        
