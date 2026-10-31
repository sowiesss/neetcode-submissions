class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, target, chosen):
            if target == 0:
                res.append(chosen.copy())
            
            for i in range(start, len(candidates)):
                if target - candidates[i] < 0:
                    break
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                chosen.append(candidates[i])
                backtrack(i + 1, target - candidates[i], chosen)
                chosen.pop()

        backtrack(0, target, [])
        return res