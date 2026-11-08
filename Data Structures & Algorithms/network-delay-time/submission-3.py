class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) < n - 1:
            return -1

        dist = [math.inf] * (n + 1)
        dist[k] = 0

        for _ in range(n - 1):
            for s, e, t in times:
                if dist[s] < math.inf and dist[s] + t < dist[e]:
                    dist[e] = dist[s] + t
        
        res = max(dist[1:])

        return res if res < math.inf else -1
