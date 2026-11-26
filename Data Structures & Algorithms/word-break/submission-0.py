class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        def dfs(l, r):
            if l >= n:
                return True
            if r >= n:
                return False
            
            res = False
            for w in wordDict:
                if s[l: r + 1] == w:
                    if dfs(r + 1, r + 1):
                        res = True

            if dfs(l, r + 1):
                res = True

            dp[l][r] = res
            return res

        return dfs(0, 0)