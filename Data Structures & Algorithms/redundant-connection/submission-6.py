class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)
            degree[e] += 1
            degree[s] += 1
        
        q = []
        for i in range(1, n + 1):
            if degree[i] == 1:
                q.append(i)

        while q:
            node = q.pop(0)
            degree[node] = 0
            for nei in adj[node]:
                if degree[nei]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        cycle = set()
        for i in range(1, n + 1):
            if degree[i]:
                cycle.add(i)
    
        for s, e in edges[::-1]:
            if s in cycle and e in cycle:
                return [s, e]

        return []

