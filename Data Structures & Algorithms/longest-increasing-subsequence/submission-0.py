class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[-1] = 1

        def dfs(i):
            if i >= n:
                return 0
            if dp[i] > 0:
                return dp[i]
            if nums[i] < nums[i + 1]:
                dp[i] = 1 + dfs(i + 1)
            else:
                dp[i] = dfs(i + 1)
            return dp[i]
        
        return dfs(0)

        