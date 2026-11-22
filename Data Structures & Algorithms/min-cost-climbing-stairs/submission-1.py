class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        c = [-1] * n
        
        def climb(floor):
            if floor >= n:
                return 0
            if c[floor] >= 0:
                return c[floor]
            c[floor] = cost[floor] + min(climb(floor + 1), climb(floor + 2))
            return c[floor]
        
        return min(climb(0), climb(1))