class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        visit = [0] * (n + 1)
        cycle = set()
        start = -1
        def dfs(node, par):
            nonlocal start
            visit[node] = 1
            for nei in adj[node]:
                if nei == par:
                    continue
                if visit[nei]:
                    start = nei
                    cycle.add(nei)
                    cycle.add(node)
                    return False
                if not dfs(nei, node):
                    if start > 0:
                        if node == start:
                            start = -1
                        else:
                            cycle.add(node)
                    return False
            return True

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)
            
        if not dfs(1, -1):
            if start > 0:
                cycle.add(1)

        for s, e in edges[::-1]:
            if s in cycle and e in cycle:
                return [s, e]

        return []

