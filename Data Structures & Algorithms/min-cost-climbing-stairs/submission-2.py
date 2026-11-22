class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        def climb(floor, c):
            if floor >= n:
                return c
            return min(climb(floor + 1, c + cost[floor]),
                        climb(floor + 2, c + cost[floor]))
        
        return min(climb(0, 0), climb(1, 0))