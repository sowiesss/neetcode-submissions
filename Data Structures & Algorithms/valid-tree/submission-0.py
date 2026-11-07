class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visit = [0] * n

        def dfs(node, par):
            if visit[node]:
                return False
            
            visit[node] = 1
            for n in adj[node]:
                if n != par and not dfs(n, node):
                    return False
            return True

        return dfs(0, -1)

        