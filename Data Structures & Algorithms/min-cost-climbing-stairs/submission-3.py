class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        c = [-1] * (n + 1)
        c[1], c[0] = 0, 0
        for i in range(n - 1):
            c[i + 2] = min(cost[i] + c[i], cost[i + 1] + c[i + 1])
        return c[n]
