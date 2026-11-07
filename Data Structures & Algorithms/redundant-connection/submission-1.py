class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        visit = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]


        def dfs(node, par):
            visit[node] = 1
            for nei in adj[node]:
                if nei == par:
                    continue
                if visit[nei]:
                    return False
                res = dfs(nei, node)
                if not res:
                    return False
            return True

        res = []
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)
            if not dfs(e, s):
                res = [s, e]

        return res

