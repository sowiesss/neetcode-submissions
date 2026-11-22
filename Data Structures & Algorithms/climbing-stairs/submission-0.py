class Solution:
    def climbStairs(self, n: int) -> int:

        def count(steps):
            if steps <= 2:
                return steps
            return count(steps - 1) + count(steps - 2)
            
        return count(n)
        