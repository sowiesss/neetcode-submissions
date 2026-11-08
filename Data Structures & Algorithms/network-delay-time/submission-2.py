class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) < n - 1:
            return -1

        dist = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for s, e, t in times:
            dist[s - 1][e - 1] = t

        for m in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][m] + dist[m][j])
        
        res = max(dist[k - 1])

        return res if res < math.inf else -1
