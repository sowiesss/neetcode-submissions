"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        stk = [node]
        while stk:
            n = stk.pop()
            if n not in visited:
                c = Node(n.val)
                visited[n] = c
                for nbr in n.neighbors:
                    stk.append(nbr)
                    if nbr not in visited:
                        cnbr = Node(nbr.val)
                        visited[nbr] = cnbr
                        c.neighbors.append(cnbr)
                    else:
                        c.neighbors.append(visited[nbr])
            else:
                c = visited[n]
                for nbr in n.neighbors:
                    
                    if nbr not in visited:
                        cnbr = Node(nbr.val)
                        visited[nbr] = cnbr
                        c.neighbors.append(cnbr)
                        stk.append(nbr)
                    elif visited[nbr] not in c.neighbors:
                        c.neighbors.append(visited[nbr])

        return visited[node]
        