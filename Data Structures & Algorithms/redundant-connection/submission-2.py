class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]


        def dfs(node, par):
            visit[node] = 1
            for nei in adj[node]:
                if nei == par:
                    continue
                if visit[nei]:
                    return False
                if not dfs(nei, node):
                    return False
            return True

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)
            visit = [0] * (n + 1)
            if not dfs(e, -1):
                return [s, e]

        return []

