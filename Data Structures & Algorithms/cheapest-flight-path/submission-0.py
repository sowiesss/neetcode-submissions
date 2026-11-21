class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for fr, to, price in flights:
            adj[fr].append((price, to))

        q = deque([(0, src)])
        stop = 0
        cost = [math.inf] * n
        while q:
            if stop > k + 1:
                break
            for _ in range(len(q)):
                c, a = q.popleft()
                
                if cost[a] > c:
                    cost[a] = c
                    for price, nei in adj[a]:
                        q.append((c + price, nei))

            stop += 1
        return cost[dst] if cost[dst] < math.inf else -1

