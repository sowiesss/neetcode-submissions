class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2
        dp = [[False] * (half + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(1, half + 1):
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]


        return dp[n - 1][half]


       