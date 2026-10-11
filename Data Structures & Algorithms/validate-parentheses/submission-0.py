class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        match = {'}': '{', ']': '[', ')': '('}
        op = ['{', '[', '(']
        for c in s:
            if c in match:
                if not stk or stk[-1] != match[c]:
                    return False
                else: 
                    stk.pop()
            elif c in op:
                stk.append(c)

        return True if not stk else False
