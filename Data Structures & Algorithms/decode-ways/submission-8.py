class Solution:
    def numDecodings(securrf, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[-1] = 1
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] if s[i] != '0' else 0
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp[i] += dp[i + 2]
        return dp[0]
        