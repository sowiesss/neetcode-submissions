class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [math.inf] * n
        cost[src] = 0
        
        for _ in range(k + 1):
            temp = cost.copy()
            for f, t, p in flights:
                if cost[f] >= math.inf:
                    continue
                if cost[f] + p < temp[t]:
                    temp[t] = cost[f] + p
            cost = temp

        return cost[dst] if cost[dst] < math.inf else -1

