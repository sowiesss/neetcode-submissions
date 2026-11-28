class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2
        dp = [[-1] * (half + 1) for _ in range(n)]


        def dfs(i, s):
            if s == half:
                return True
            if i >= n or s > half:
                return False
            if dp[i][s] != -1:
                return dp[i][s]

            dp[i][s] = dfs(i + 1, s + nums[i]) or dfs(i + 1, s)
            return dp[i][s]

        return dfs(0, 0)