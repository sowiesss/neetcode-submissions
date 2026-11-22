class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for fr, to, price in flights:
            adj[fr].append((price, to))

        q = deque([src])
        stop = 0
        cost = [math.inf] * n
        cost[src] = 0
        visit = [False] * n
        while q and stop <= k:
            temp = cost.copy()
            for _ in range(len(q)):
                node = q.popleft()
                visit[node] = False
                for price, nei in adj[node]:
                    if cost[node] + price < temp[nei]:
                        temp[nei] = cost[node] + price
                        if not visit[nei]:
                            visit[nei] = True
                            q.append(nei)
            cost = temp
            stop += 1
        return cost[dst] if cost[dst] < math.inf else -1

