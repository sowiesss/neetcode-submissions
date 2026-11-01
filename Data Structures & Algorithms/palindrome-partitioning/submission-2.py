class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        
        def palindrome(part: List[str], start: int):
            if start >= n:
                res.append(part.copy())
                return
            
            for i in range(start, n):
                if valid(start, i):
                    part.append(s[start:i + 1])
                    palindrome(part, i + 1)
                    part.pop()
            

        def valid(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        
        palindrome([], 0)
        return res