class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        cnt = [0] * (n + 1)
        cnt[0] = 0
        cnt[1] = 1
        cnt[2] = 2
        for i in range(3, n + 1):
            cnt[i] = cnt[i - 1] + cnt[i - 2]
        
        return cnt[n]
        