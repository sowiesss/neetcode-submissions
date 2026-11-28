class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def dfs(i, s1, s2):
            if i >= n:
                return s1 == s2
            o1 = dfs(i + 1, s1 + nums[i], s2)
            o2 = dfs(i + 1, s1, s2 + nums[i])
            return o1 or o2

        return dfs(0, 0, 0)