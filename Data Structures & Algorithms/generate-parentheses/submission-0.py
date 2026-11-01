class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(state, open, close):
            if len(state) == 2 * n:
                res.append(state)
                return
            
            if open < n:
                state += '('
                backtrack(state, open + 1, close)
                state = state[:-1]

            if close < open:
                state += ')'
                backtrack(state, open, close + 1)
                state = state[:-1]
        
        backtrack('', 0, 0)
        return res

        