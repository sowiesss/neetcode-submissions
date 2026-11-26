class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def dfs(l, r):
            if l >= n:
                return 1
            if r >= n:
                return 0
            if dp[l][r] >= 0:
                return dp[l][r]
            
            res = 0
            for w in wordDict:
                if s[l: r + 1] == w:
                    if dfs(r + 1, r + 1):
                        res = 1

            if dfs(l, r + 1):
                res = 1

            dp[l][r] = res
            return res

        dfs(0, 0)

        return True if dp[0][0] > 0 else False