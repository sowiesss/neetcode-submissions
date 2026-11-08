class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) < n - 1:
            return -1

        dist = [math.inf] * (n + 1)
        dist[k] = 0
        
        adj = defaultdict(list)
        for s, e, t in times:
            adj[s].append((e, t))

        heap = [(0, k)]
        while heap:
            t, u = heapq.heappop(heap)
            if dist[u] < t:
                continue
            for end, time in adj[u]:
                if dist[end] > dist[u] + time:
                    dist[end] = dist[u] + time
                    heapq.heappush(heap, (dist[end], end))

        print(dist)
        res = max(dist[1:])

        return res if res < math.inf else -1
