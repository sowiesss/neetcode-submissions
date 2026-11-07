class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visit = [0] * n
        q = [(0, -1)]
        while q:
            node, p = q.pop(0)
            if visit[node]:
                return False

            visit[node] = 1
            for nei in adj[node]:
                if nei == p:
                    continue
                if visit[nei]:
                    return False
                else:
                    q.append((nei, node))
        
        return sum(visit) == n
 

        