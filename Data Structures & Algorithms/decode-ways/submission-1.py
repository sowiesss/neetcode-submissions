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

            curr = int(s[i])
            if curr > 2 or (curr == 2 and i < n - 1 and int(s[i + 1]) > 6):
                print(i, "+1")
                dp[i] = dfs(i + 1)
                return dp[i]
            
            if i < n - 1 and int(s[i + 1]) ==  0:
                print(i, "+2")
                dp[i] = dfs(i + 2)
                return dp[i]

            dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]

        
        
        print(dp)
        return dfs(0)
        