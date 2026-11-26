class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        n = len(coins)
        dp = {}

        def dfs(need):
            if need == 0:
                return 0
            if need in dp:
                return dp[need]
            res = math.inf
            for c in coins:
                if c <= need:
                    res = min(res, dfs(need - c) + 1)
            dp[need] = res
            return res

        r = dfs(amount)
        return r if r < math.inf else -1

            
            
        