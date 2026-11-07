class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visit = [0] * n

        def dfs(node):
            visit[node] = 1
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)

        cnt = 0
        for i in range(n):
            if not visit[i]:
                cnt += 1
                dfs(i)

        return cnt
