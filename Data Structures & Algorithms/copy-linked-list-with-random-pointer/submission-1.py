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
        curr = head
        while curr:
            n = Node(curr.val)
            dic[curr] = n
            curr = curr.next
        
        curr = head
        while curr:
            copy = dic[curr]
            if curr.random:
                copy.random = dic[curr.random]
            if curr.next:
                copy.next = dic[curr.next]
            curr = curr.next

        return dic[head]

        