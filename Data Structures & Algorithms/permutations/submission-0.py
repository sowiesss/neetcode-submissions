class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        select = [0] * n

        def backtrack(state):
            if len(state) == n:
                res.append(state.copy())
            
            for i in range(n):
                if select[i]:
                    continue
                state.append(nums[i])
                select[i] = 1
                backtrack(state)
                state.pop()
                select[i] = 0

        backtrack([])
        return res