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
        visited[node] = Node(node.val)
        q = [node]
        while q:
            n = q.pop(0)
            copy = visited[n]
            for nei in n.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    q.append(nei)
                copy.neighbors.append(visited[nei])

        return visited[node]
        