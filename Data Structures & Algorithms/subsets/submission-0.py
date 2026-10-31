class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, chosen):
            res.append(list(chosen))
            for i in range(start, len(nums)):
                chosen.append(nums[i])
                backtrack(i + 1, chosen)
                chosen.pop()

        backtrack(0, [])
        return res