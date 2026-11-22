class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        cnt = [0] * (n + 1)
        cnt[0] = 0
        cnt[1] = 1
        cnt[2] = 2

        def count(steps):
            if steps <= 2:
                return steps
            if cnt[steps] > 0:
                return cnt[steps]
            cnt[steps] = count(steps - 1) + count(steps - 2)
            return cnt[steps]
        
        return count(n)
        