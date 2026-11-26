class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1] * n

        def dfs(start):
            if start == n:
                return 1
            if dp[start] >= 0:
                return dp[start]
            
            for w in wordDict:
                end = len(w) + start
                if end <= n and s[start: end] == w:
                    if dfs(end) == 1:
                        dp[start] = 1
                        return dp[start]

            dp[start] = 0
            return dp[start]

        dfs(0)

        return True if dp[0] > 0 else False