class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1] * n

        def dfs(start):
            if start == n:
                return 1
            if dp[start] >= 0:
                return dp[start]
            
            res = 0
            for w in wordDict:
                l = len(w)
                if s[start: start + l] == w:
                    if dfs(start + l) == 1:
                        res = 1

            dp[start] = res
            return res

        dfs(0)

        return True if dp[0] > 0 else False