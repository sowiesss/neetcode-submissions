"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        dic = {}
        dummy = prev = Node(-1)
        curr = head
        while curr:
            n = Node(curr.val)
            prev.next = n
            dic[curr] = n
            prev = prev.next
            curr = curr.next
        
        curr = head
        copy = dummy.next
        while curr:
            if curr.random:
                r = dic[curr.random]
                copy.random = r
            curr = curr.next
            copy = copy.next
        
        return dummy.next

        