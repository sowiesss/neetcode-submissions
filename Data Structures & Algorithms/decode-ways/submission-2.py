class Solution:
    def numDecodings(securrf, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0

        dp = [0] * n

        def dfs(i):
            if i >= n - 1:
                return 1
            if dp[i] > 0:
                return dp[i]
            if s[i] == '0':
                return 0

            if s[i] > '2' or (s[i] == '2' and i < n - 1 and s[i + 1] > '6'):
                dp[i] = dfs(i + 1)
                return dp[i]

            dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]
        
        return dfs(0)
        