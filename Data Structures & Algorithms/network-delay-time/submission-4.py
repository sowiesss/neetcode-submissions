class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) < n - 1:
            return -1

        dist = [math.inf] * (n + 1)
        dist[k] = 0

        adj = defaultdict(list)
        for s, e, t in times:
            adj[s].append((e, t))

        visit = [0] * (n + 1)
        q = deque([k])
        while q:
            u = q.popleft()
            for end, time in adj[u]:
                if dist[end] > dist[u] + time:
                    dist[end] = dist[u] + time
                    if not visit[end]:
                        visit[end] = 1
                        q.append(end)

        res = max(dist[1:])

        return res if res < math.inf else -1
