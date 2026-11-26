class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def dfs(i, j):
            if i >= n:
                return 0
            if dp[i][j + 1] > 0:
                return dp[i][j + 1]

            dp[i][j + 1] = dfs(i + 1, j)

            if j == -1 or nums[i] > nums[j]:
                dp[i][j + 1] = max(dp[i][j + 1], 1 + dfs(i + 1, i))
            
            return dp[i][j + 1]
        
        dfs(0, -1)
    
        return dp[0][0]

        