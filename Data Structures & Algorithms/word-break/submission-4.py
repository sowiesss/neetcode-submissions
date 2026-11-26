class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1] * n
        wordset = set(wordDict)
        t = 0
        for w in wordDict:
            t = max(t, len(w))

        def dfs(start):
            if start == n:
                return 1
            if dp[start] >= 0:
                return dp[start]
            
            for i in range(start, min(n, start + t)):
                if s[start: i + 1] in wordset:
                    if dfs(i + 1) == 1:
                        dp[start] = 1
                        return dp[start]

            dp[start] = 0
            return dp[start]

        dfs(0)

        return True if dp[0] > 0 else False