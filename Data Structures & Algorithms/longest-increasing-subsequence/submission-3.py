class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def dfs(i):
            if i >= n:
                return 0
            if dp[i] > 0:
                return dp[i]

            res = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, dfs(j) + 1)
            dp[i] = res
            return res
        
        return max(dfs(i) for i in range(n))

        