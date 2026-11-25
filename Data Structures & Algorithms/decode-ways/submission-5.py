class Solution:
    def numDecodings(securrf, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0

        dp = [0] * n

        def dfs(i):
            if i >= n:
                return 1
            if dp[i] > 0:
                return dp[i]
            if s[i] == '0':
                return 0

            res = dfs(i + 1)
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and i < n - 1 and s[i + 1] < '7')):
                res += dfs(i + 2)
            dp[i] = res
            return dp[i]
        
        return dfs(0)
        