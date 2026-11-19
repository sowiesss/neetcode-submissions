class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        heap = [(0, 0, 0)]
        res = 0
        while heap:
            w, v1, v2 = heapq.heappop(heap)
            if visited[v1] and visited[v2]:
                continue
            res += w
            visited[v1] = True
            visited[v2] = True
            for i in range(n):
                if visited[i]:
                    continue
                dis1 = abs(points[i][0] - points[v1][0]) + abs(points[i][1] - points[v1][1])
                dis2 = abs(points[i][0] - points[v2][0]) + abs(points[i][1] - points[v2][1])
                if dis1 < dis2:
                    heapq.heappush(heap, (dis1, v1, i))
                else:
                    heapq.heappush(heap, (dis2, v2, i))

        return res
