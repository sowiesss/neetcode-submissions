class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visit = [0] * n

        def bfs(node):
            visit[node] = 1
            q = [node]
            while q:
                curr = q.pop(0)
                for nei in adj[curr]:
                    if not visit[nei]:
                        q.append(nei)
                        visit[nei] = 1

        cnt = 0
        for i in range(n):
            if not visit[i]:
                cnt += 1
                bfs(i)

        return cnt
