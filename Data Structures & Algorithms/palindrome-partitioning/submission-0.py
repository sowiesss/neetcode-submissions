class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        

        def palindrome(part: List[str], start: int, end:int):
            if start >= len(s):
                res.append(part.copy())
                return

            if valid(s[start: end]):
                part.append(s[start: end])
                palindrome(part, end, end + 1)
                part.pop()
            
            if end < len(s):
                palindrome(part, start, end + 1)
            

        def valid(s1: str):
            n = len(s1)
            for i in range(n // 2):
                if s1[i] != s1[n - i - 1]:
                    return False
            return True

        
        palindrome([], 0, 1)
        return res