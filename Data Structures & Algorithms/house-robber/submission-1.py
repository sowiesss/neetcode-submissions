class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxs = [0] * n
        
        def dfs(i):
            if i >= n:
                return 0
            maxsuff = max(dfs(i + 2), dfs(i + 3))
            maxs[i] = nums[i] + maxsuff
            return maxs[i]

        dfs(0)
        dfs(1)
        return max(maxs[0], maxs[1])
            