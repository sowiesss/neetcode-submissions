class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        maxs = [0] * n
        
        def dfs(i):
            if i >= n:
                return 0
            if maxs[i] > 0:
                return maxs[i]
            maxsuff = max(dfs(i + 2), dfs(i + 3))
            maxs[i] = nums[i] + maxsuff
            return maxs[i]

        dfs(0)
        dfs(1)
        return max(maxs[0], maxs[1])
            