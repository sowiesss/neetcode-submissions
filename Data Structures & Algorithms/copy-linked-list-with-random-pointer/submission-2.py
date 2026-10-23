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
            if curr not in dic:
                copy = Node(curr.val)
                dic[curr] = copy
            else:
                copy = dic[curr]

            if curr.next and curr.next not in dic:
                nxt = Node(curr.next.val)
                copy.next = nxt
                dic[curr.next] = nxt
            elif curr.next:
                copy.next= dic[curr.next]

            if curr.random and curr.random not in dic:
                ran = Node(curr.random.val)
                dic[curr.random] = ran
                copy.random = ran
            elif curr.random:
                copy.random = dic[curr.random]
                
            curr = curr.next

        return dic[head]

        