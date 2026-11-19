class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return t
            if visited[r][c]:
                continue
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    time = max(t, grid[nr][nc])
                    heapq.heappush(heap, (time, nr, nc))
        
        return 0
            
