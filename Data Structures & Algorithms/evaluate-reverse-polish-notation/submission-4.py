class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for c in tokens:
            if c == '+':
                s = stk.pop() + stk.pop()
                stk.append(s)

            elif c == '*':
               p = stk.pop() * stk.pop()
               stk.append(p)

            elif c == '-':
                op2 = stk.pop()
                op1 = stk.pop()
                d = op1 - op2
                stk.append(d)
            
            elif c == '/':
                op2 = stk.pop()
                op1 = stk.pop()
                q = op1 // op2
                stk.append(q)
            
            else:
                stk.append(int(c))

        return stk[0]

