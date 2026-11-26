class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        n = len(coins)
        coins.sort(reverse=True)
        dp = [{} for _ in range(n)]

        def dfs(i, need):
            temp = need
            if need == 0:
                return 0
            if i >= n:
                return -1
            if need in dp[i]:
                return dp[i][need]

            cnt = 0
            while coins[i] <= need:
                cnt += 1
                need -= coins[i]
                res =  dfs(i + 1, need)
                if res >= 0:
                    if temp in dp[i] and dp[i][temp] > res + cnt:
                        dp[i][temp] = cnt + res
                    elif temp not in dp[i]:
                        dp[i][temp] = cnt + res
            res =  dfs(i + 1, need)
            if res >= 0:
                if temp in dp[i] and dp[i][temp] > res + cnt:
                    dp[i][temp] = cnt + res
                elif temp not in dp[i]:
                    dp[i][temp] = cnt + res
            if temp not in dp[i]:
                return -1
           
            return dp[i][temp]

        return dfs(0, amount)
                

            
            
        