class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        d_to_l = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }


        def backtrack(ind, s):
            if ind == n:
                if s:
                    res.append(s)
                return

            for c in d_to_l[digits[ind]]:
                backtrack(ind + 1, s + c) # pass a new str
            

        backtrack(0, "")
        return res
