class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxs = 0
        
        def dfs(i, s):
            nonlocal maxs
            if i >= n:
                return s
            s += nums[i]
            maxs = max(maxs, dfs(i + 2, s), dfs(i + 3, s))
            return maxs

        dfs(0, 0)
        dfs(1, 0)
        return maxs
            