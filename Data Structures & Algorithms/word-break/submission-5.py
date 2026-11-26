class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for st in range(n - 1, -1, -1):
            for w in wordDict:
                e = len(w) + st
                if e <= n and s[st:e] == w:
                    dp[st] = dp[e]
                    if dp[st]:
                        break
        return dp[0]