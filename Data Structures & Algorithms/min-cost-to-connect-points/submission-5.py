class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i][j] = dis
                adj[j][i] = dis

        visited = [False] * n
        dis = [math.inf] * n
        node = 0
        res = 0
        cnt = 0
        while cnt < n - 1:
            visited[node] = True
            newN = -1
            for i in range(n):
                if visited[i]:
                    continue
                dis[i] = min(dis[i], adj[node][i])   
                if newN < 0 or dis[i] < dis[newN]:
                    newN = i
            node = newN
            cnt += 1
            res += dis[node]
        return res
