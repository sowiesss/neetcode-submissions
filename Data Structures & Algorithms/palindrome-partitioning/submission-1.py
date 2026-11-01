class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def palindrome(part: List[str], start: int, end:int):
            if start >= len(s):
                res.append(part.copy())
                return
            
            if end >= len(s):
                return

            if valid(s, start, end):
                part.append(s[start: end + 1])
                palindrome(part, end + 1, end + 1)
                part.pop()
            
            palindrome(part, start, end + 1)
            

        def valid(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        
        palindrome([], 0, 0)
        return res