class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2
        dp = [False] * (half + 1)
        dp[0] = True

        for n in nums:
            nexDp = dp.copy()
            for s in range(1, half + 1):
                if n <= s:
                    nexDp[s] = dp[s] or dp[s - n]
                else:
                    nexDp[s] = dp[s]
            dp = nexDp


        return dp[half]


       