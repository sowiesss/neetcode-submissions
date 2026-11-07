class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) < n - 1:
            return -1

        timebook = defaultdict(list)
        
        for ui, vi, ti in times:
            timebook[ui].append((vi, ti))

        visit = [0] * (n + 1)
        time = 0
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if visit[node]:
                continue
            visit[node] = 1
            if sum(visit) == n:
                break
            for nei, ti in timebook[node]:
                if not visit[nei]:
                    heapq.heappush(heap, (time + ti, nei))

        return time if sum(visit) == n else -1



        