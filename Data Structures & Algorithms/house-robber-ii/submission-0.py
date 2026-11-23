class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [-1] * n

        def dfs(i):
            if i >= n:
                return 0
            if i == n - 1:
                dp[i] = nums[i] if not first else 0
                return dp[i]
            if dp[i] >= 0:
                return dp[i]

            dp[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
            return dp[i]
        
        first = True
        dfs(0)
        first = False
        dfs(1)
        return max(dp[0], dp[1])
            
        