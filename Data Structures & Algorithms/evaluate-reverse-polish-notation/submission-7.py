class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        c = tokens.pop()
        
        if c in '+-*/':
            r = self.evalRPN(tokens)
            l = self.evalRPN(tokens)

            match c:
                case '-':
                    return l - r
                case '+':
                    return l + r
                case '*':
                    return l * r
                case '/':
                    return int(l / r)
        else:
            return int(c)



