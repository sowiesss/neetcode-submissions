class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [-1] * n

        def dfs(i, first):
            if i >= n:
                return 0
            if dp[i] >= 0:
                return dp[i]
            if i == n - 1:
                dp[i] = nums[i] if not first else 0
                return dp[i]
            if i == 0 and not first:
                dp[i] = max(dfs(i + 1, first), dfs(i + 2, first))
                return dp[i]

            dp[i] = max(dfs(i + 1, first), dfs(i + 2, first) + nums[i])
            return dp[i]
        
        res1 = dfs(0, True)
        print(dp)
        dp = [-1] * n
        res2 = dfs(0, False)
        print(dp)
        return max(res1, res2)
            
        