class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}
        def dfs(i, s1, s2):
            if i >= n:
                return s1 == s2
            if (i, s1, s2) in dp:
                return dp[(i, s1, s2)]
            o1 = dfs(i + 1, s1 + nums[i], s2)
            o2 = dfs(i + 1, s1, s2 + nums[i])
            dp[(i, s1, s2)] = o1 or o2
            return dp[(i, s1, s2)]

        return dfs(0, 0, 0)