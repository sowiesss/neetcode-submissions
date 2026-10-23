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
        dic = defaultdict(lambda: Node(0))
        dic[None] = None

        curr = head
        while curr:
            copy = dic[curr]
            copy.val = curr.val
            copy.next = dic[curr.next]
            copy.random = dic[curr.random]
            curr = curr.next
        return dic[head]

        