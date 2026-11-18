class DSU:
    def __init__(self, size):
        self.parent = [x for x in range(size)]
        self.size = [1] * size

    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]


    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        if self.size[p1] > self.size[p2]:
            p1, p2 = p2, p1
        
        self.size[p2] += self.size[p1]
        self.parent[p1] = p2
        return True



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [[False] * n for _ in range(n)]
        edges = []
        dsu = DSU(n)

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
        res = 0
        cnt = 0
        for w, v1, v2 in edges:
            if dsu.union(v1, v2):
                res += w
                cnt += 1
                if cnt == n - 1:
                    break

        return res
