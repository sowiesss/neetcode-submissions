class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [[False] * n for _ in range(n)]
        edges = []

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if visited[i][j]:
                    continue
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dis, i, j))
                visited[i][j] = True
                visited[j][i] = True

        edges.sort()
        included = [False] * n
        res = 0
        cnt = 0
        for w, v1, v2 in edges:
            if included[v1] and included[v2]:
                continue
            res += w
            cnt += 1
            if cnt == n - 1:
                break
            included[v1] = True
            included[v2] = True

        return res
