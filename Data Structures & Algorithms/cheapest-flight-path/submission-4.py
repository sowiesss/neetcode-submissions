class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])
        
        dist = [[math.inf] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        heap = [(0, src, 0)]

        while heap:
            cost, city, stop = heapq.heappop(heap)
            if city == dst: return cost
            if stop == k + 1 or dist[city][stop] < cost:
                continue
            for nei, price in adj[city]:
                ncost = price + cost
                nstop = stop + 1
                if dist[nei][nstop] > ncost:
                    dist[nei][nstop] = ncost
                    heapq.heappush(heap, (ncost, nei, nstop))

        return -1

