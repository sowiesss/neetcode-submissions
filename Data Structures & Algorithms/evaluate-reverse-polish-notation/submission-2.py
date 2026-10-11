class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        res = 0
        for c in tokens:
            if c == '+':
                s = int(stk.pop()) + int(stk.pop())
                stk.append(s)

            elif c == '*':
               p = int(stk.pop()) * int(stk.pop())
               stk.append(p)

            elif c == '-':
                op2 = int(stk.pop())
                op1 = int(stk.pop())
                d = op1 - op2
                stk.append(d)
            
            elif c == '/':
                op2 = int(stk.pop())
                op1 = int(stk.pop())
                q = op1 / op2
                res += q
                stk.append(q)
            
            else:
                stk.append(c)

        return stk[0] if len(tokens) > 1 else int(tokens[0])

